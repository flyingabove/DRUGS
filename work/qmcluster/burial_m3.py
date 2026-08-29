# -*- coding: utf-8 -*-
"""Per-atom burial of GPX4-M3 in its own best anchored pose.
Tests the core design premise directly: do the N-methylamide arms - the ONLY thing
we changed from ML210 - sit in solvent, or do they touch protein?"""
import numpy as np
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem
RDLogger.DisableLog('rdApp.*')
VDW={'C':1.70,'N':1.55,'O':1.52,'S':1.80,'Se':1.90,'H':1.20,'F':1.47,'Cl':1.75}
rec=[];sec_se=None
for l in open('../structures/6HKQ_receptor.pdb'):
    if not l.startswith(('ATOM','HETATM')): continue
    nm=l[12:16].strip();rn=l[17:20].strip();el=(l[76:78].strip() or nm[0]).capitalize()
    if el=='H': continue
    p=np.array([float(l[30:38]),float(l[38:46]),float(l[46:54])])
    if rn in ('SEC','CSE') and nm=='SE': sec_se=p; continue
    if rn in ('SEC','CSE') and nm=='CB': continue
    rec.append(p)
assert sec_se is not None
R=np.array(rec); R=R[np.linalg.norm(R-sec_se,axis=1)<20]
sup=Chem.SDMolSupplier('../structures/G9N_bound.sdf',removeHs=True,sanitize=False)
GP=next(iter(sup)).GetConformer().GetPositions()
d=np.linalg.norm(GP-sec_se,axis=1);VEC=(GP[int(np.argmin(d))]-sec_se)/np.linalg.norm(GP[int(np.argmin(d))]-sec_se)
ADD={'ML210':'O=C(N1CCN(C(c2ccc(Cl)cc2)c2ccc(Cl)cc2)CC1)C(=N[O-])[Se]C',
     'GPX4-M3':'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)C(=N[O-])[Se]C)CC2)cc1'}
def sasa_burial(X,EL,probe=1.4,npts=180):
    """fraction of each atom's SA sphere occluded by receptor atoms"""
    g=np.arange(npts);phi=np.arccos(1-2*(g+0.5)/npts);th=np.pi*(1+5**0.5)*g
    U=np.c_[np.cos(th)*np.sin(phi),np.sin(th)*np.sin(phi),np.cos(phi)]
    out=[]
    for i,(x,e) in enumerate(zip(X,EL)):
        r=VDW.get(e,1.7)+probe; S=x+U*r
        near=R[np.linalg.norm(R-x,axis=1)<r+2.0]
        if len(near)==0: out.append(0.0); continue
        D=np.linalg.norm(S[:,None,:]-near[None,:,:],axis=2)
        occ=(D<(1.7+probe)).any(axis=1)
        out.append(occ.mean())
    return np.array(out)
def best_pose(smi,nconf=140):
    m=Chem.AddHs(Chem.MolFromSmiles(smi))
    cids=list(AllChem.EmbedMultipleConfs(m,numConfs=nconf,randomSeed=2024,pruneRmsThresh=0.6))
    try: AllChem.MMFFOptimizeMoleculeConfs(m,maxIters=500)
    except Exception: pass
    sei=[a.GetIdx() for a in m.GetAtoms() if a.GetSymbol()=='Se'][0]
    nb=[n.GetIdx() for n in m.GetAtomWithIdx(sei).GetNeighbors()]
    ci=max(nb,key=lambda i:sum(1 for x in m.GetAtomWithIdx(i).GetNeighbors() if x.GetSymbol()!='H'))
    EL=[a.GetSymbol() for a in m.GetAtoms()];hv=[i for i,e in enumerate(EL) if e!='H']
    RV=np.array([1.7]*len(R));best=(1e9,None)
    for c in cids:
        P=m.GetConformer(c).GetPositions();v=P[ci]-P[sei];v/=np.linalg.norm(v)
        cr=np.cross(v,VEC);dp=np.dot(v,VEC)
        K=np.array([[0,-cr[2],cr[1]],[cr[2],0,-cr[0]],[-cr[1],cr[0],0]])
        Rm=np.eye(3)+K+K@K*((1-dp)/(np.linalg.norm(cr)**2)) if np.linalg.norm(cr)>1e-8 else np.eye(3)
        Q=(P-P[sei])@Rm.T
        for ang in np.linspace(0,2*np.pi,48,endpoint=False):
            ca=np.cos(ang);k=VEC
            K2=np.array([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])
            Rr=np.eye(3)*ca+np.sin(ang)*K2+(1-ca)*np.outer(k,k)
            X=Q@Rr.T+sec_se
            L=X[hv];D=np.linalg.norm(L[:,None,:]-R[None,:,:],axis=2)
            ov=float(((np.array([VDW.get(EL[i],1.7) for i in hv])[:,None]+RV[None,:]-0.5)-D).max())
            if ov<best[0]: best=(ov,X.copy())
    return m,EL,best[1],best[0]
print("PER-ATOM BURIAL IN THE ANCHORED POSE  (0 = fully solvent-exposed, 1 = fully buried)\n")
for n,s in ADD.items():
    m,EL,X,ov=best_pose(s)
    hv=[i for i,e in enumerate(EL) if e!='H']
    b=sasa_burial(X[hv],[EL[i] for i in hv])
    # locate the modified arms: amide N/O/C of the CONHMe groups (M3 only)
    patt=Chem.MolFromSmarts('[CX3](=O)[NX3][CH3]')
    mm=Chem.MolFromSmiles(s); hits=mm.GetSubstructMatches(patt) if mm else []
    print("%-9s  overlap %.2f A | mean burial %.2f | atoms >50%% buried: %d/%d"%(
        n,ov,b.mean(),(b>0.5).sum(),len(b)))
    srt=np.argsort(b)
    print("           most exposed: "+", ".join("%s%d %.2f"%(EL[hv[i]],hv[i],b[i]) for i in srt[:5]))
    print("           most buried : "+", ".join("%s%d %.2f"%(EL[hv[i]],hv[i],b[i]) for i in srt[-5:]))
    if n=='GPX4-M3':
        np.save('m3_pose_full.npy',X)
        with open('m3_pose_elements.txt','w') as fh:
            fh.write(chr(10).join(EL))
        print("           -> saved m3_pose_full.npy (%d atoms, incl. H)"%len(X))

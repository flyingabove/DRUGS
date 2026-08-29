# -*- coding: utf-8 -*-
"""Anchored covalent fit v2. Two controls:
   (a) the crystal ligand in its DEPOSITED POSE -> empirical tolerable overlap
   (b) the same ligand re-derived by conformer search -> validates the protocol"""
import numpy as np, json
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem
RDLogger.DisableLog('rdApp.*')
VDW={'C':1.70,'N':1.55,'O':1.52,'S':1.80,'Se':1.90,'H':1.20,'F':1.47,'Cl':1.75,'Br':1.85}
TOL=0.5
rec=[];sec_se=None;sec_res=None
for l in open('../structures/6HKQ_receptor.pdb'):
    if not l.startswith(('ATOM','HETATM')): continue
    nm=l[12:16].strip(); rn=l[17:20].strip(); el=(l[76:78].strip() or nm[0]).capitalize()
    if el=='H': continue
    p=np.array([float(l[30:38]),float(l[38:46]),float(l[46:54])])
    # Rule 1: assert the CATALYTIC residue explicitly. Matching any CYS/SG picks Cys10.
    if rn in ('SEC','CSE') and nm=='SE': sec_se=p; sec_res=(rn,l[22:26].strip()); continue
    if rn in ('SEC','CSE') and nm=='CB': continue
    rec.append((el,p))
assert sec_se is not None, "catalytic Sec not found"
print("catalytic site: %s%s SE at %s"%(sec_res[0],sec_res[1],np.round(sec_se,2)))
R=np.array([p for _,p in rec]); RV=np.array([VDW.get(e,1.7) for e,_ in rec])
# prune: only atoms within 18 A of Se can clash with a ~15 A ligand anchored there
_m=np.linalg.norm(R-sec_se,axis=1)<18.0
R=R[_m]; RV=RV[_m]
print("receptor atoms within 18 A of Se: %d (from %d)"%(len(R),len(_m)))
def overlap(X,EL):
    LV=np.array([VDW.get(e,1.7) for e in EL])
    D=np.linalg.norm(X[:,None,:]-R[None,:,:],axis=2)
    return float(((LV[:,None]+RV[None,:]-TOL)-D).max())
# ---- (a) crystal ligand, deposited pose
sup=Chem.SDMolSupplier('../structures/G9N_bound.sdf',removeHs=True,sanitize=False)
g=next(iter(sup)); GP=g.GetConformer().GetPositions(); GE=[a.GetSymbol() for a in g.GetAtoms()]
keep=[i for i,e in enumerate(GE) if e!='H']
ov_xtal=overlap(GP[keep],[GE[i] for i in keep])
assert min(np.linalg.norm(GP[keep]-sec_se,axis=1))<2.5, "ligand is NOT bonded to the identified Se - wrong site"
d=[np.linalg.norm(p-sec_se) for p in GP[keep]]; ci=int(np.argmin(d))
VEC=(GP[keep][ci]-sec_se)/np.linalg.norm(GP[keep][ci]-sec_se)
print("CALIBRATION")
print("  crystal ligand G9N, DEPOSITED POSE      max overlap = %.2f A   (closest atom %.2f A from Se)"%(ov_xtal,d[ci]))
print("  Se->C attack vector %s\n"%np.round(VEC,3))
ADD={
 'G9N_reconstructed':'COc1ccc(N(C(=O)C[Se]C)[C@@H](C(=O)NCCc2ccccc2)c2cccs2)cc1Cl',
 'ML210'            :'O=C(N1CCN(C(c2ccc(Cl)cc2)c2ccc(Cl)cc2)CC1)C(=N[O-])[Se]C',
 'GPX4-M3 (prev)'   :'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)C(=N[O-])[Se]C)CC2)cc1',
 'GPX4-C1 (new)'    :'O=C(N1CCN(C(c2ccccc2)c3ccccc3)CC1)C(=N[O-])[Se]C',
 'GPX4-C4 (new)'    :'O=C(N1CC(=O)N(C(c2ccccc2)c3ccccc3)CC1)C(=N[O-])[Se]C',
}
def fit(smi,nconf=120):
    m=Chem.MolFromSmiles(smi)
    if m is None: return None
    m=Chem.AddHs(m)
    cids=list(AllChem.EmbedMultipleConfs(m,numConfs=nconf,randomSeed=2024,pruneRmsThresh=0.6))
    try: AllChem.MMFFOptimizeMoleculeConfs(m,maxIters=500)
    except Exception: pass
    sei=[a.GetIdx() for a in m.GetAtoms() if a.GetSymbol()=='Se'][0]
    nb=[n.GetIdx() for n in m.GetAtomWithIdx(sei).GetNeighbors()]
    ci=max(nb,key=lambda i:sum(1 for x in m.GetAtomWithIdx(i).GetNeighbors() if x.GetSymbol()!='H'))
    EL=[a.GetSymbol() for a in m.GetAtoms()]
    hv=[i for i,e in enumerate(EL) if e!='H' and i!=sei]
    ELh=[EL[i] for i in hv]
    best=1e9
    for c in cids:
        P=m.GetConformer(c).GetPositions()
        v=P[ci]-P[sei]; v/=np.linalg.norm(v)
        cr=np.cross(v,VEC); dp=np.dot(v,VEC)
        if np.linalg.norm(cr)<1e-8: Rm=np.eye(3)
        else:
            K=np.array([[0,-cr[2],cr[1]],[cr[2],0,-cr[0]],[-cr[1],cr[0],0]])
            Rm=np.eye(3)+K+K@K*((1-dp)/(np.linalg.norm(cr)**2))
        Q=(P-P[sei])@Rm.T
        for ang in np.linspace(0,2*np.pi,48,endpoint=False):
            ca=np.cos(ang); k=VEC
            K=np.array([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])
            Rr=np.eye(3)*ca+np.sin(ang)*K+(1-ca)*np.outer(k,k)
            X=(Q@Rr.T+sec_se)[hv]
            o=overlap(X,ELh)
            if o<best: best=o
    return best,len(cids)
print("CONFORMER-SEARCHED ADDUCTS")
print("%-20s %8s %14s   %s"%("compound","confs","overlap (A)","note"))
print("-"*70)
out={'crystal_pose':round(ov_xtal,2)}
for n,s in ADD.items():
    r=fit(s)
    if r is None: print("  %-20s SMILES failed"%n); continue
    o,nc=r; out[n]=round(o,2)
    note=("PROTOCOL CONTROL - should match crystal" if n.startswith('G9N') else
          ("NEW LEAD" if n=='GPX4-M3' else ""))
    print("%-20s %8d %14.2f   %s"%(n,nc,o,note))
json.dump(out,open('fit_v2.json','w'),indent=1); print("\n-> fit_v2.json")

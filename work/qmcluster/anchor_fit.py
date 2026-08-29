# -*- coding: utf-8 -*-
"""Anchored covalent fit, calibrated (rebuild of the sec-16 protocol, now saved).
Rule 15: Sec46 SE and CB are COVALENT PARTNERS and must be excluded from the clash test.
Rule 12: ML162 is the positive control - it is the ligand present in 6HKQ."""
import numpy as np, subprocess, re, json, os, sys
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem
RDLogger.DisableLog('rdApp.*')

VDW={'C':1.70,'N':1.55,'O':1.52,'S':1.80,'Se':1.90,'H':1.20,'F':1.47,'Cl':1.75}
TOL=0.5

# ---- receptor heavy atoms from the ligand-bound structure, ligand removed
rec=[];sec_se=None;sec_cb=None
for l in open('../structures/6HKQ_receptor.pdb'):
    if not l.startswith(('ATOM','HETATM')): continue
    nm=l[12:16].strip(); rn=l[17:20].strip(); el=(l[76:78].strip() or nm[0]).capitalize()
    if el=='H': continue
    p=np.array([float(l[30:38]),float(l[38:46]),float(l[46:54])])
    if rn in ('SEC','CYS','CSE') and nm=='SE': sec_se=p
    if rn in ('SEC','CYS','CSE') and nm=='CB' and sec_se is None: sec_cb=p
    rec.append((el,p,nm,rn))
se=np.load('se.npy')
if sec_se is None: sec_se=se
# exclude the covalent partner atoms (Rule 15)
keep=[(el,p) for el,p,nm,rn in rec if not (np.linalg.norm(p-sec_se)<0.1 or (nm=='CB' and np.linalg.norm(p-sec_se)<2.5))]
R=np.array([p for _,p in keep]); RV=np.array([VDW.get(el,1.7) for el,_ in keep])
print("receptor heavy atoms: %d  (excluded %d covalent-partner atoms)  Se at %s"%(len(R),len(rec)-len(keep),np.round(sec_se,2)))

# ---- crystallographic Se->C attack vector from the bound ligand
lig=[np.array([float(l[30:38]),float(l[38:46]),float(l[46:54])])
     for l in open('../structures/6HKQ_ligand.pdb') if l.startswith(('ATOM','HETATM')) and (l[76:78].strip() or 'C')!='H']
d=[np.linalg.norm(p-sec_se) for p in lig]; cidx=int(np.argmin(d))
VEC=(lig[cidx]-sec_se)/np.linalg.norm(lig[cidx]-sec_se)
print("crystallographic Se->C vector %s  (bond %.2f A)"%(np.round(VEC,3),d[cidx]))

CPDS={
 'ML162_ctrl':'CC(Sc1ccccc1)C(=O)N(Cc1ccccc1)C(C(=O)OC)c1ccccc1',
 'ML210':'O=C(N1CCN(C(c2ccc(Cl)cc2)c2ccc(Cl)cc2)CC1)c1noc(C)c1[N+](=O)[O-]',
 'GPX4-M1':'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2CCN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'GPX4-M3':'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
}
def adduct_smiles(name,smi):
    """Attach C[Se] to the electrophilic carbon. Ring-closure digits vary between
    compounds (1 vs 3), so match them with a backreference rather than literally."""
    pat=re.compile(r'C\(=O\)c(\d)noc\(C\)c\[N\+\]\(=O\)\[O-\]')
    if pat.search(smi):
        return pat.sub('C(=O)C(=[N+][O-])[Se]C',smi,count=1)
    return smi.replace('CC(Sc1ccccc1)','CC([Se]C)(Sc1ccccc1)',1)

def build_opt(name,smi,nconf=160):
    a=adduct_smiles(name,smi); m=Chem.MolFromSmiles(a)
    if m is None: print("  %-12s adduct SMILES failed: %s"%(name,a)); return None
    m=Chem.AddHs(m)
    cids=AllChem.EmbedMultipleConfs(m,numConfs=nconf,randomSeed=2024,pruneRmsThresh=0.5)
    try: AllChem.MMFFOptimizeMoleculeConfs(m,maxIters=400)
    except Exception: pass
    return m,list(cids)

def fit(name,smi):
    r=build_opt(name,smi)
    if r is None: return None
    m,cids=r
    sei=[a.GetIdx() for a in m.GetAtoms() if a.GetSymbol()=='Se']
    if not sei: print("  %-12s no Se in adduct"%name); return None
    sei=sei[0]
    # the warhead carbon bonded to Se (not the methyl)
    nb=[n.GetIdx() for n in m.GetAtomWithIdx(sei).GetNeighbors()]
    ci=max(nb,key=lambda i:m.GetAtomWithIdx(i).GetDegree())
    elems=[a.GetSymbol() for a in m.GetAtoms()]
    heavy=[i for i,e in enumerate(elems) if e!='H' and i!=sei]
    LV=np.array([VDW.get(elems[i],1.7) for i in heavy])
    best=(1e9,None)
    for c in cids:
        P=m.GetConformer(c).GetPositions()
        v=P[ci]-P[sei]; v/=np.linalg.norm(v)
        # rotation taking v -> VEC
        a_,b_=v,VEC; cr=np.cross(a_,b_); dp=np.dot(a_,b_)
        if np.linalg.norm(cr)<1e-8: Rm=np.eye(3)
        else:
            K=np.array([[0,-cr[2],cr[1]],[cr[2],0,-cr[0]],[-cr[1],cr[0],0]])
            Rm=np.eye(3)+K+K@K*((1-dp)/(np.linalg.norm(cr)**2))
        Q=(P-P[sei])@Rm.T
        for ang in np.linspace(0,2*np.pi,60,endpoint=False):
            ca,sa=np.cos(ang),np.sin(ang); k=VEC
            K=np.array([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])
            Rr=np.eye(3)*ca+np.sin(ang)*K+(1-ca)*np.outer(k,k)
            X=Q@Rr.T+sec_se
            L=X[heavy]
            D=np.linalg.norm(L[:,None,:]-R[None,:,:],axis=2)
            ov=(LV[:,None]+RV[None,:]-TOL)-D
            mx=float(ov.max())
            if mx<best[0]: best=(mx,c)
    return best[0],len(cids)

print("\nANCHORED COVALENT FIT — calibrated against the ligand present in the crystal\n")
print("%-14s %10s %16s"%("compound","conformers","max overlap (A)"))
print("-"*44)
out={}
for n,s in CPDS.items():
    r=fit(n,s)
    if r is None: continue
    ov,nc=r; out[n]=[nc,round(ov,2)]
    tag=" <-- POSITIVE CONTROL (crystal ligand)" if n=='ML162_ctrl' else (" <-- NEW LEAD" if n=='GPX4-M3' else "")
    print("%-14s %10d %16.2f%s"%(n,nc,ov,tag))
json.dump(out,open('fit_M3.json','w'),indent=1)

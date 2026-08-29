# -*- coding: utf-8 -*-
"""Tier 1.2/1.3 - build Nu(-) + nitrile-oxide complexes for relaxed distance scans."""
import numpy as np, os
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem
RDLogger.DisableLog('rdApp.*')
PT=Chem.GetPeriodicTable()

ELEC='CN(C)C(=O)C#[N+][O-]'          # model electrophile: acyl nitrile oxide (unmasked warhead)
NUCS={'Se':'[CH3][Se-]','S':'[CH3][S-]'}

def emb(smi,seed=42):
    m=Chem.AddHs(Chem.MolFromSmiles(smi))
    AllChem.EmbedMolecule(m,randomSeed=seed); AllChem.MMFFOptimizeMolecule(m)
    return m

def coords(m): return m.GetConformer().GetPositions()

e=emb(ELEC); ec=coords(e)
# locate the nitrile-oxide carbon: C triple-bonded to N
ci=None
for b in e.GetBonds():
    if b.GetBondType()==Chem.BondType.TRIPLE:
        a1,a2=b.GetBeginAtom(),b.GetEndAtom()
        if a1.GetSymbol()=='C' and a2.GetSymbol()=='N': ci,ni=a1.GetIdx(),a2.GetIdx()
        if a2.GetSymbol()=='C' and a1.GetSymbol()=='N': ci,ni=a2.GetIdx(),a1.GetIdx()
assert ci is not None, 'no nitrile oxide C found'
# R group carbon attached to the electrophilic C
ri=[n.GetIdx() for n in e.GetAtomWithIdx(ci).GetNeighbors() if n.GetIdx()!=ni][0]
print("electrophilic C idx=%d  (triple-bond N=%d, R=%d)"%(ci,ni,ri))

# attack direction: where a 3rd sp2 substituent would sit
u1=ec[ri]-ec[ci]; u1/=np.linalg.norm(u1)
u2=ec[ni]-ec[ci]; u2/=np.linalg.norm(u2)
d=-(u1+u2); d/=np.linalg.norm(d)

R0=3.60
for tag,smi in NUCS.items():
    n=emb(smi); nc=coords(n)
    hi=[a.GetIdx() for a in n.GetAtoms() if a.GetSymbol()==tag][0]
    mi=[a.GetIdx() for a in n.GetAtoms() if a.GetSymbol()=='C'][0]
    # orient nucleophile: heteroatom toward C, methyl pointing away
    v=nc[hi]-nc[mi]; v/=np.linalg.norm(v)
    # rotation aligning v -> -d  (so heteroatom leads)
    a,b=v,-d; vv=np.cross(a,b); c=np.dot(a,b)
    if np.linalg.norm(vv)<1e-8: Rm=np.eye(3)*(1 if c>0 else -1)
    else:
        K=np.array([[0,-vv[2],vv[1]],[vv[2],0,-vv[0]],[-vv[1],vv[0],0]])
        Rm=np.eye(3)+K+K@K*((1-c)/(np.linalg.norm(vv)**2))
    nc2=(nc-nc[hi])@Rm.T + ec[ci]+d*R0
    syms=[a.GetSymbol() for a in e.GetAtoms()]+[a.GetSymbol() for a in n.GetAtoms()]
    xyz=np.vstack([ec,nc2])
    nu_idx=len(ec)+hi   # 0-based
    with open('cx_%s.xyz'%tag,'w') as f:
        f.write("%d\ncomplex %s  attackC=%d nu=%d\n"%(len(syms),tag,ci+1,nu_idx+1))
        for s,p in zip(syms,xyz): f.write("%-3s %12.6f %12.6f %12.6f\n"%(s,p[0],p[1],p[2]))
    with open('scan_%s.inp'%tag,'w') as f:
        f.write("$constrain\n force constant=0.75\n distance: %d, %d, auto\n$scan\n 1: 3.60,1.90,22\n$end\n"%(ci+1,nu_idx+1))
    print("  %s: wrote cx_%s.xyz (%d atoms), scan %d-%d"%(tag,tag,len(syms),ci+1,nu_idx+1))

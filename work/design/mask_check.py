# -*- coding: utf-8 -*-
"""Rule 5 check: do the new polar groups stay AVAILABLE to water, or fold back onto
the molecule? 2D descriptors cannot see this. An earlier bis-hydroxyethyl analog (M2)
counted 2 HBD on paper and had ZERO free donors once optimised in water."""
import subprocess, re, os
import numpy as np
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem
RDLogger.DisableLog('rdApp.*')
C={
 'M3 (current)'            :'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'S1 bis-hydroxyethylamide':'OCCNC(=O)c1ccc(C(c2ccc(C(=O)NCCO)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'S3 bis-primary amide'    :'NC(=O)c1ccc(C(c2ccc(C(=O)N)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'S4 bis-sulfonamide'      :'CNS(=O)(=O)c1ccc(C(c2ccc(S(=O)(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
}
def analyse(name,smi,nconf=40):
    m=Chem.AddHs(Chem.MolFromSmiles(smi))
    cids=list(AllChem.EmbedMultipleConfs(m,numConfs=nconf,randomSeed=42,pruneRmsThresh=0.5))
    try: AllChem.MMFFOptimizeMoleculeConfs(m,maxIters=800)
    except Exception: pass
    # donors: O-H and N-H
    donors=[]
    for a in m.GetAtoms():
        if a.GetSymbol() in ('O','N'):
            for nb in a.GetNeighbors():
                if nb.GetSymbol()=='H': donors.append((a.GetIdx(),nb.GetIdx()))
    acceptors=[a.GetIdx() for a in m.GetAtoms()
               if (a.GetSymbol()=='O') or (a.GetSymbol()=='N' and a.GetTotalNumHs()==0)]
    free_counts=[]
    for c in cids:
        P=m.GetConformer(c).GetPositions()
        free=0
        for (d,h) in donors:
            masked=False
            for acc in acceptors:
                if acc==d: continue
                dh=np.linalg.norm(P[h]-P[acc])
                if dh<2.5:   # H...acceptor within H-bond range
                    v1=P[h]-P[d]; v2=P[acc]-P[h]
                    ang=np.degrees(np.arccos(np.clip(np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2)),-1,1)))
                    if ang<60: masked=True; break
            if not masked: free+=1
        free_counts.append(free)
    return len(donors),float(np.mean(free_counts)),min(free_counts),max(free_counts),len(cids)
print("INTRAMOLECULAR MASKING CHECK — are the polar groups actually available to water?\n")
print("%-26s %8s %10s %8s %8s"%("compound","donors","mean free","min","max"))
print("-"*66)
for n,s in C.items():
    nd,mean,lo,hi,nc=analyse(n,s)
    flag='' if mean>nd*0.6 else '  <-- MASKED'
    print("%-26s %8d %10.2f %8d %8d%s"%(n,nd,mean,lo,hi,flag))
print("""
  'donors' = O-H and N-H groups on paper.
  'free'   = those still pointing at solvent after 3D optimisation, per conformer.
  A large gap means the group folds back onto the molecule and does NOT help solubility,
  even though every 2D descriptor still counts it.""")

# -*- coding: utf-8 -*-
"""RULE 12 positive control + clean thermodynamics, consistently referenced.
Control: SN2  CH3-Br + Nu(-) -> CH3-Nu + Br(-).  Selenolate is EXPERIMENTALLY the
stronger nucleophile; if the protocol says otherwise it is broken."""
import os,subprocess,re,numpy as np
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem
RDLogger.DisableLog('rdApp.*')
H=627.5094740631
def xtb_E(smi,chrg,tag,solv='water'):
    m=Chem.AddHs(Chem.MolFromSmiles(smi))
    cids=AllChem.EmbedMultipleConfs(m,numConfs=8,randomSeed=0xf00d)
    try: AllChem.MMFFOptimizeMoleculeConfs(m)
    except Exception: pass
    best=None
    for c in cids:
        p=m.GetConformer(c).GetPositions(); s=[a.GetSymbol() for a in m.GetAtoms()]
        fn='%s_%d.xyz'%(tag,c)
        with open(fn,'w') as f:
            f.write("%d\n\n"%len(s))
            for a,q in zip(s,p): f.write("%-3s %12.6f %12.6f %12.6f\n"%(a,q[0],q[1],q[2]))
        r=subprocess.run(['xtb',fn,'--gfn','2','--alpb',solv,'--chrg',str(chrg),'--opt','tight'],
                         capture_output=True,text=True,errors='ignore')
        mm=re.findall(r'TOTAL ENERGY\s+(-?\d+\.\d+)',r.stdout)
        if mm:
            e=float(mm[-1])
            if best is None or e<best: best=e
    return best
S={}
sp=[('MeSeH_anion','[CH3][Se-]',-1),('MeSH_anion','[CH3][S-]',-1),
    ('MeBr','CBr',0),('Br_anion','[Br-]',-1),
    ('MeSeMe','C[Se]C',0),('MeSMe','CSC',0),
    ('elec','CN(C)C(=O)C#[N+][O-]',0),
    ('add_Se','CN(C)C(=O)C(=[N+][O-])[Se]C',-1),
    ('add_S','CN(C)C(=O)C(=[N+][O-])SC',-1)]
for t,smi,c in sp:
    S[t]=xtb_E(smi,c,t); print("  %-12s %-34s chg%+d  E=%s"%(t,smi,c,("%.6f"%S[t]) if S[t] else "FAIL"))
print("\n"+"="*70)
print("POSITIVE CONTROL — SN2:  CH3Br + Nu(-)  ->  CH3Nu + Br(-)")
for nu,adt,nut in [('Se','MeSeMe','MeSeH_anion'),('S','MeSMe','MeSH_anion')]:
    dE=(S[adt]+S['Br_anion'])-(S['MeBr']+S[nut])
    print("   Nu = %-3s   dE_rxn = %+8.2f kcal/mol"%(nu,dE*H))
    S['ctl_'+nu]=dE*H
d=S['ctl_Se']-S['ctl_S']
print("   selenolate - thiolate = %+.2f kcal/mol  -> %s"%(d,
   "Se MORE reactive: matches experiment, PROTOCOL OK" if d<0 else "Se LESS reactive: CONTRADICTS EXPERIMENT -> PROTOCOL SUSPECT"))
print("\n"+"="*70)
print("TARGET REACTION — nitrile oxide + Nu(-) -> adduct  (thermodynamics)")
for nu,adt,nut in [('Se','add_Se','MeSeH_anion'),('S','add_S','MeSH_anion')]:
    dE=(S[adt]-(S['elec']+S[nut]))*H
    print("   Nu = %-3s   dE_rxn = %+8.2f kcal/mol"%(nu,dE)); S['rx_'+nu]=dE
dd=S['rx_Se']-S['rx_S']
print("   ddE (Se - S) = %+.2f kcal/mol  -> %s"%(dd,"selenolate favoured" if dd<0 else "thiolate favoured"))

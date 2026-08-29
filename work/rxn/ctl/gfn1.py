# -*- coding: utf-8 -*-
import subprocess,re,math
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem
RDLogger.DisableLog('rdApp.*')
H=627.5094740631
def E(smi,chrg,tag):
    m=Chem.AddHs(Chem.MolFromSmiles(smi))
    cids=AllChem.EmbedMultipleConfs(m,numConfs=6,randomSeed=11)
    try: AllChem.MMFFOptimizeMoleculeConfs(m)
    except Exception: pass
    best=None
    for c in cids:
        p=m.GetConformer(c).GetPositions(); s=[a.GetSymbol() for a in m.GetAtoms()]
        fn='g_%s_%d.xyz'%(tag,c)
        open(fn,'w').write("%d\n\n"%len(s)+"".join("%-3s %12.6f %12.6f %12.6f\n"%(a,q[0],q[1],q[2]) for a,q in zip(s,p)))
        r=subprocess.run(['xtb',fn,'--gfn','1','--alpb','water','--chrg',str(chrg),'--opt','tight'],
                         capture_output=True,text=True,errors='ignore')
        mm=re.findall(r'TOTAL ENERGY\s+(-?\d+\.\d+)',r.stdout)
        if mm:
            e=float(mm[-1])
            if best is None or e<best: best=e
    return best
sp={'MeSe-':('[CH3][Se-]',-1),'MeS-':('[CH3][S-]',-1),'elec':('CN(C)C(=O)C#[N+][O-]',0),
    'aSe':('CN(C)C(=O)C(=[N+][O-])[Se]C',-1),'aS':('CN(C)C(=O)C(=[N+][O-])SC',-1)}
V={k:E(s,c,k.replace('-','m')) for k,(s,c) in sp.items()}
dSe=(V['aSe']-V['elec']-V['MeSe-'])*H; dS=(V['aS']-V['elec']-V['MeS-'])*H
print("TARGET REACTION at GFN1 (the level that passed the control)\n")
print("  nitrile oxide + MeSe-  ->  adduct   dE = %+8.2f kcal/mol"%dSe)
print("  nitrile oxide + MeS-   ->  adduct   dE = %+8.2f kcal/mol"%dS)
print("  ddE (Se - S) = %+.2f kcal/mol  -> %s favoured\n"%(dSe-dS,"SELENOLATE" if dSe<dS else "thiolate"))
print("  CAVEAT: GFN1 passed the SIGN test but its absolute SN2 energies were off by")
print("  ~70 kcal/mol. Treat this as an ORDERING, not a barrier. It is not the number.\n")
print("="*72)
print("WHAT IS SOLID WITHOUT QM — the protonation-state argument (Tier 1.4)\n")
pH=7.4
for nm,pka,n in [('Sec46 selenocysteine (GPX4)',5.2,1),('generic cysteine',8.3,200000)]:
    frac=1/(1+10**(pka-pH))
    print("  %-30s pKa %.1f -> %6.2f%% anionic at pH 7.4   x%-8s = %.3g reactive sites"%(
        nm,pka,100*frac,("%.0e"%n),frac*n))
print("""
  Selenocysteine is ~99%% deprotonated and reactive; cysteine only ~11%%.
  BUT 11%% of 200,000 cysteines still vastly outnumbers one selenolate.
  => Population alone does NOT deliver selectivity. The masking kinetics must.
     And that is precisely the number this hardware cannot compute.""")

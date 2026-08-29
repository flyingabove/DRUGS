# -*- coding: utf-8 -*-
import subprocess,re
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem
RDLogger.DisableLog('rdApp.*')
H=627.5094740631
def E(smi,chrg,tag,args):
    m=Chem.AddHs(Chem.MolFromSmiles(smi)); AllChem.EmbedMolecule(m,randomSeed=7); AllChem.MMFFOptimizeMolecule(m)
    p=m.GetConformer().GetPositions(); s=[a.GetSymbol() for a in m.GetAtoms()]
    fn='d_%s.xyz'%tag
    open(fn,'w').write("%d\n\n"%len(s)+"".join("%-3s %12.6f %12.6f %12.6f\n"%(a,q[0],q[1],q[2]) for a,q in zip(s,p)))
    r=subprocess.run(['xtb',fn,'--chrg',str(chrg),'--opt','tight']+args,capture_output=True,text=True,errors='ignore')
    mm=re.findall(r'TOTAL ENERGY\s+(-?\d+\.\d+)',r.stdout)
    return float(mm[-1]) if mm else None
SP=[('MeSe-','[CH3][Se-]',-1),('MeS-','[CH3][S-]',-1),('MeBr','CBr',0),
    ('Br-','[Br-]',-1),('MeSeMe','C[Se]C',0),('MeSMe','CSC',0)]
SETUPS=[('GFN2 + ALPB water',['--gfn','2','--alpb','water']),
        ('GFN2 gas phase',    ['--gfn','2']),
        ('GFN1 + ALPB water', ['--gfn','1','--alpb','water']),
        ('GFN1 gas phase',    ['--gfn','1'])]
print("CONTROL REACTION:  CH3Br + Nu(-) -> CH3Nu + Br(-)")
print("EXPECTED: selenolate MORE reactive than thiolate  =>  d(Se-S) should be NEGATIVE\n")
print("%-22s %12s %12s %12s   %s"%("method","dE(Se)","dE(S)","d(Se-S)","verdict"))
print("-"*78)
for name,args in SETUPS:
    v={}
    for t,smi,c in SP: v[t]=E(smi,c,t.replace('-','m'),args)
    if any(x is None for x in v.values()): print("%-22s  FAILED"%name); continue
    dSe=((v['MeSeMe']+v['Br-'])-(v['MeBr']+v['MeSe-']))*H
    dS =((v['MeSMe'] +v['Br-'])-(v['MeBr']+v['MeS-'] ))*H
    d=dSe-dS
    print("%-22s %12.2f %12.2f %12.2f   %s"%(name,dSe,dS,d,"OK" if d<0 else "*** WRONG SIGN ***"))

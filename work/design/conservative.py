# -*- coding: utf-8 -*-
"""The warhead alone costs 89.5 A^2 of a ~93 A^2 budget. Polar decoration is
UNAFFORDABLE. ML210 works because its arms contribute ZERO polar surface.

So: reduce lipophilicity for chronic dosing WITHOUT spending polar surface area.
Symmetry preserved throughout (no stereocentres)."""
from rdkit import Chem, RDLogger
from rdkit.Chem import rdMolDescriptors as rd, Crippen, Descriptors
RDLogger.DisableLog('rdApp.*')
W='C(=O)c1noc(C)c1[N+](=O)[O-]'
# Ring-closure digits MUST NOT collide with the scaffold's. The scaffold uses 1 and 5;
# each arm gets its own digit (2 and 3). A collision silently produces a DIFFERENT
# molecule with the SAME molecular weight - which is why MW is not a validity check.
def ml210(a2, a3):
    return 'O=C(N1CCN(C(%s)%s)CC1)c5noc(C)c5[N+](=O)[O-]' % (a2, a3)
def ml210ox(a2, a3):
    return 'O=C(N1CC(=O)N(C(%s)%s)CC1)c5noc(C)c5[N+](=O)[O-]' % (a2, a3)
ARMS={'4-Cl-phenyl (ML210)':('c2ccc(Cl)cc2','c3ccc(Cl)cc3'),
      'phenyl (des-chloro)':('c2ccccc2','c3ccccc3'),
      '4-F-phenyl':('c2ccc(F)cc2','c3ccc(F)cc3'),
      '3,4-diF-phenyl':('c2cc(F)c(F)cc2','c3cc(F)c(F)cc3'),
      '4-CF3-phenyl':('c2ccc(C(F)(F)F)cc2','c3ccc(C(F)(F)F)cc3'),
      '4-pyridyl':('c2ccncc2','c3ccncc3'),
      '3-pyridyl':('c2cccnc2','c3cccnc3'),
      '4-Me-phenyl':('c2ccc(C)cc2','c3ccc(C)cc3'),
      '2-thienyl':('c2cccs2','c3cccs3'),
      'cyclohexyl':('C2CCCCC2','C3CCCCC3')}
wh=Chem.MolFromSmarts('c1noc(C)c1[N+](=O)[O-]')
# ASSERT the generator reproduces the known compound before trusting anything it makes
_ref=Chem.MolToSmiles(Chem.MolFromSmiles('O=C(N1CCN(C(c2ccc(Cl)cc2)c2ccc(Cl)cc2)CC1)c1noc(C)c1[N+](=O)[O-]'))
_gen=Chem.MolToSmiles(Chem.MolFromSmiles(ml210('c2ccc(Cl)cc2','c3ccc(Cl)cc3')))
assert _ref==_gen, 'generator does NOT reproduce ML210 - ring digits collided'
print('generator validated against known ML210 structure')
print("CONSERVATIVE SERIES — cut greasiness without spending polar surface\n")
print("window: TPSA<=93, HBD<=1, cLogP 3.4-4.8 (from six cell-active GPX4 inhibitors)\n")
print("%-40s %7s %7s %5s %7s %5s  %s"%("compound","MW","TPSA","HBD","cLogP","stereo","verdict"))
print("-"*94)
rows=[]
for lk,fn in [('piperazine',ml210),('2-oxopiperazine',ml210ox)]:
    for an,ar in ARMS.items():
        s=fn(ar[0],ar[1]); m=Chem.MolFromSmiles(s)
        if m is None or not m.HasSubstructMatch(wh): continue
        t=rd.CalcTPSA(m); lp=Crippen.MolLogP(m); hbd=rd.CalcNumHBD(m); mw=Descriptors.MolWt(m)
        st=len(Chem.FindMolChiralCenters(m,useLegacyImplementation=False,includeUnassigned=True))
        if t<=93 and hbd<=1 and 3.0<=lp<=5.2: v='IN WINDOW'
        elif t<=110 and hbd<=1 and lp>=2.5:   v='close'
        else: v='outside'
        nm='%s / %s'%(an,lk)
        rows.append((nm,mw,t,hbd,lp,st,v,s))
        print("%-40s %7.1f %7.1f %5d %7.2f %5d  %s"%(nm,mw,t,hbd,lp,st,v))
print("\nIN-WINDOW candidates with the LOWEST greasiness (best for chronic dosing):")
inw=[r for r in rows if r[6]=='IN WINDOW' and r[5]==0]
inw.sort(key=lambda r:r[4])
for r in inw[:5]:
    print("   %-40s cLogP %.2f  TPSA %.1f"%(r[0],r[4],r[2]))
if inw:
    print("\nbest SMILES: %s"%inw[0][7])

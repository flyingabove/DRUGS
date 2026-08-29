# -*- coding: utf-8 -*-
"""Full workup on the new leads, matching what GPX4-M3 received."""
from rdkit import Chem, RDLogger
from rdkit.Chem import Descriptors, rdMolDescriptors as rd, Crippen, QED
import sys, os
sys.path.append(os.path.join(os.environ.get('CONDA_PREFIX',''),'share','RDKit','Contrib','SA_Score'))
try: import sascorer
except Exception: sascorer=None
RDLogger.DisableLog('rdApp.*')
C={
 'ML210 (parent)'   :'O=C(N1CCN(C(c2ccc(Cl)cc2)c2ccc(Cl)cc2)CC1)c1noc(C)c1[N+](=O)[O-]',
 'GPX4-C1'          :'O=C(N1CCN(C(c2ccccc2)c3ccccc3)CC1)c5noc(C)c5[N+](=O)[O-]',
 'GPX4-C4'          :'O=C(N1CC(=O)N(C(c2ccccc2)c3ccccc3)CC1)c5noc(C)c5[N+](=O)[O-]',
 'GPX4-C2 (bis-4-F)':'O=C(N1CCN(C(c2ccc(F)cc2)c3ccc(F)cc3)CC1)c5noc(C)c5[N+](=O)[O-]',
 'GPX4-M3 (prev)'   :'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
}
wh=Chem.MolFromSmarts('c1noc(C)c1[N+](=O)[O-]')
basic=Chem.MolFromSmarts("[NX3;H0,H1,H2;!$(N[C,S]=[O,S,N]);!$(N[a]);!$(N[N,O]);!$(N#*)]")
SOFT=[("benzylic CH","[CX4H1,CX4H2]([c])[c]"),("N-methyl amide","[CH3][NX3][CX3]=O"),
      ("aryl-Cl","[c][Cl]"),("CH2 alpha to N","[CH2]-[NX3]")]
def props(m):
    return dict(mw=Descriptors.MolWt(m),lp=Crippen.MolLogP(m),tpsa=rd.CalcTPSA(m),
        rb=rd.CalcNumRotatableBonds(m),ar=rd.CalcNumAromaticRings(m),hbd=rd.CalcNumHBD(m),
        ap=sum(1 for a in m.GetAtoms() if a.GetIsAromatic())/max(1,m.GetNumHeavyAtoms()))
def esol(p): return 0.16-0.63*p['lp']-0.0062*p['mw']+0.066*p['rb']-0.74*p['ap']
def ali(p):  return -1.0374-1.0116*p['lp']+0.0080*p['tpsa']-0.0102*p['mw']+0.4373
def mpt(p):  return 25+40*p['ar']+18*p['hbd']+0.25*p['tpsa']-12*p['rb']
def gse(p):  return 0.5-0.01*(mpt(p)-25.0)-p['lp']
print("FULL WORKUP — matching what GPX4-M3 received\n")
print("%-20s %6s %6s %6s %4s %5s %6s %6s %8s %8s"%("compound","MW","cLogP","TPSA","HBD","basN","stereo","SA","mg/mL","hERG"))
print("-"*94)
for n,s in C.items():
    m=Chem.MolFromSmiles(s)
    if m is None or not m.HasSubstructMatch(wh): print("  %-20s INVALID/warhead broken"%n); continue
    p=props(m); nb=len(m.GetSubstructMatches(basic))
    st=len(Chem.FindMolChiralCenters(m,useLegacyImplementation=False,includeUnassigned=True))
    mean=(esol(p)+ali(p)+gse(p))/3; mg=(10**mean)*p['mw']
    ar=rd.CalcNumAromaticRings(m)
    herg=(nb>0)*2+(ar>=2)*1+(p['lp']>3.5)*1
    hl={0:'low',1:'low',2:'moderate',3:'MOD-HIGH',4:'HIGH'}[min(herg,4)]
    sa=sascorer.calculateScore(m) if sascorer else float('nan')
    print("%-20s %6.1f %6.2f %6.1f %4d %5d %6d %6.2f %8.4f %8s"%(n,p['mw'],p['lp'],p['tpsa'],p['hbd'],nb,st,sa,mg,hl))
print("\nCYP SOFT SPOTS")
for n,s in C.items():
    m=Chem.MolFromSmiles(s)
    if m is None: continue
    h=[(l,len(m.GetSubstructMatches(Chem.MolFromSmarts(sm)))) for l,sm in SOFT]
    print("  %-20s %s"%(n,", ".join("%s x%d"%(l,c) for l,c in h if c) or "none"))
print("\nPERMEABILITY vs revised ceiling (~130 A^2 from approved covalent intracellular drugs)")
for n,s in C.items():
    m=Chem.MolFromSmiles(s)
    if m is None: continue
    t=rd.CalcTPSA(m)
    print("  %-20s TPSA %6.1f  %s"%(n,t,'INSIDE' if t<=130 else 'OUTSIDE (+%.0f)'%(t-130)))

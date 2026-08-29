# -*- coding: utf-8 -*-
"""BRANCH B: improve C4 solubility WITHIN the polarity budget.
C4 is at TPSA 109.8; ceiling from approved covalent intracellular drugs is ~130.
So there are ~20 A^2 to spend. Symmetry must be preserved (asymmetric aryls would
create a stereocentre). Warhead untouched."""
from rdkit import Chem, RDLogger
from rdkit.Chem import rdMolDescriptors as rd, Crippen, Descriptors
RDLogger.DisableLog('rdApp.*')
def build(a2,a3,linker='CC(=O)N'):
    return 'O=C(N1CC(=O)N(C(%s)%s)CC1)c5noc(C)c5[N+](=O)[O-]'%(a2,a3)
CAND={
 'C4 (current lead)'      :('c2ccccc2','c3ccccc3'),
 'D1 bis-4-OMe'           :('c2ccc(OC)cc2','c3ccc(OC)cc3'),
 'D2 bis-4-F'             :('c2ccc(F)cc2','c3ccc(F)cc3'),
 'D3 bis-3-pyridyl'       :('c2cccnc2','c3cccnc3'),
 'D4 bis-4-pyridyl'       :('c2ccncc2','c3ccncc3'),
 'D5 bis-3-OMe'           :('c2cccc(OC)c2','c3cccc(OC)c3'),
 'D6 bis-3,4-diOMe'       :('c2ccc(OC)c(OC)c2','c3ccc(OC)c(OC)c3'),
 'D7 bis-4-OCF3'          :('c2ccc(OC(F)(F)F)cc2','c3ccc(OC(F)(F)F)cc3'),
 'D8 bis-2-furyl'         :('c2ccco2','c3ccco3'),
}
wh=Chem.MolFromSmarts('c1noc(C)c1[N+](=O)[O-]')
basic=Chem.MolFromSmarts("[NX3;H0,H1,H2;!$(N[C,S]=[O,S,N]);!$(N[a]);!$(N[N,O]);!$(N#*)]")
def props(m):
    return dict(mw=Descriptors.MolWt(m),lp=Crippen.MolLogP(m),tpsa=rd.CalcTPSA(m),
        rb=rd.CalcNumRotatableBonds(m),ar=rd.CalcNumAromaticRings(m),hbd=rd.CalcNumHBD(m),
        ap=sum(1 for a in m.GetAtoms() if a.GetIsAromatic())/max(1,m.GetNumHeavyAtoms()))
def esol(p): return 0.16-0.63*p['lp']-0.0062*p['mw']+0.066*p['rb']-0.74*p['ap']
def ali(p):  return -1.0374-1.0116*p['lp']+0.0080*p['tpsa']-0.0102*p['mw']+0.4373
def mpt(p):  return 25+40*p['ar']+18*p['hbd']+0.25*p['tpsa']-12*p['rb']
def gse(p):  return 0.5-0.01*(mpt(p)-25.0)-p['lp']
print("BRANCH B — C4 solubility within the ~130 polarity budget (symmetry preserved)\n")
print("%-22s %7s %7s %6s %5s %6s %10s  %s"%("candidate","MW","TPSA","cLogP","basN","stereo","mg/mL","budget"))
print("-"*88)
base=None
for n,(a2,a3) in CAND.items():
    m=Chem.MolFromSmiles(build(a2,a3))
    if m is None or not m.HasSubstructMatch(wh): print("  %-22s INVALID"%n); continue
    p=props(m); mean=(esol(p)+ali(p)+gse(p))/3; mg=(10**mean)*p['mw']
    nb=len(m.GetSubstructMatches(basic))
    st=len(Chem.FindMolChiralCenters(m,useLegacyImplementation=False,includeUnassigned=True))
    if base is None: base=mg
    tag='OK' if p['tpsa']<=130 else 'OVER +%.0f'%(p['tpsa']-130)
    print("%-22s %7.1f %7.1f %6.2f %5d %6d %10.4f  %s  (%.1fx)"%(n,p['mw'],p['tpsa'],p['lp'],nb,st,mg,tag,mg/base))
print("""
  budget = polar surface vs the ~130 A^2 ceiling observed for approved covalent drugs
  with intracellular targets. Anything OVER risks the permeability problem again.""")

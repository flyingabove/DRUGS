# -*- coding: utf-8 -*-
"""Attack the solubility blocker. Constraints:
   - warhead untouched (it is what works and what makes it selective)
   - no basic nitrogen (that was the kidney/heart fix - do not undo it)
   - keep symmetry where possible (no stereocentres)
So: add NEUTRAL polar groups, or break planarity, without touching the warhead."""
from rdkit import Chem, RDLogger
from rdkit.Chem import Descriptors, rdMolDescriptors as rd, Crippen
RDLogger.DisableLog('rdApp.*')
W='C(=O)c3noc(C)c3[N+](=O)[O-]'
def tpl(arm,link='N2C(=O)CN(%s)CC2'):
    return 'CNC(=O)'.replace('CNC(=O)','')+arm
CANDS={
 'M3 (current)'            :'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'M1 (salt-formable)'      :'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2CCN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 # --- neutral polar arms (no charge, more H-bonding) ---
 'S1 bis-hydroxyethylamide':'OCCNC(=O)c1ccc(C(c2ccc(C(=O)NCCO)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'S2 bis-morpholinoamide'  :'O=C(N1CCOCC1)c1ccc(C(c2ccc(C(=O)N3CCOCC3)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'S3 bis-primary amide'    :'NC(=O)c1ccc(C(c2ccc(C(=O)N)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'S4 bis-sulfonamide'      :'CNS(=O)(=O)c1ccc(C(c2ccc(S(=O)(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'S5 bis-methoxyethylamide':'COCCNC(=O)c1ccc(C(c2ccc(C(=O)NCCOC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 # --- break planarity / packing ---
 'S6 3-CONHMe (meta)'      :'CNC(=O)c1cccc(C(c2cccc(C(=O)NC)c2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)c1',
 'S7 2-F ortho twist'      :'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)c(F)c2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1F',
 'S8 N-methylated amide'   :'CN(C)C(=O)c1ccc(C(c2ccc(C(=O)N(C)C)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
}
wh=Chem.MolFromSmarts('c1noc(C)c1[N+](=O)[O-]')
basic=Chem.MolFromSmarts("[NX3;H0,H1,H2;!$(N[C,S]=[O,S,N]);!$(N[a]);!$(N[N,O]);!$(N#*)]")
def props(m):
    return dict(mw=Descriptors.MolWt(m),lp=Crippen.MolLogP(m),tpsa=rd.CalcTPSA(m),
        rb=rd.CalcNumRotatableBonds(m),ar=rd.CalcNumAromaticRings(m),hbd=rd.CalcNumHBD(m),
        ap=sum(1 for a in m.GetAtoms() if a.GetIsAromatic())/max(1,m.GetNumHeavyAtoms()))
def esol(p): return 0.16-0.63*p['lp']-0.0062*p['mw']+0.066*p['rb']-0.74*p['ap']
def ali(p):  return -1.0374-1.0116*p['lp']+0.0080*p['tpsa']-0.0102*p['mw']+0.4373
def mp(p):   return 25+40*p['ar']+18*p['hbd']+0.25*p['tpsa']-12*p['rb']
def gse(p):  return 0.5-0.01*(mp(p)-25.0)-p['lp']
print("SOLUBILITY REPAIR — warhead fixed, no basic N reintroduced\n")
print("%-26s %6s %6s %5s %5s %7s %10s %6s"%("candidate","MW","cLogP","basN","stereo","logS","mg/mL","warhead"))
print("-"*86)
rows=[]
for n,s in CANDS.items():
    m=Chem.MolFromSmiles(s)
    if m is None: print("  %-26s INVALID"%n); continue
    p=props(m); mean=(esol(p)+ali(p)+gse(p))/3; mg=(10**mean)*p['mw']
    nb=len(m.GetSubstructMatches(basic))
    st=len(Chem.FindMolChiralCenters(m,useLegacyImplementation=False,includeUnassigned=True))
    ok=m.HasSubstructMatch(wh)
    rows.append((n,mg,nb,st,ok,p['lp']))
    print("%-26s %6.1f %6.2f %5d %5d %7.2f %10.4f %6s"%(n,p['mw'],p['lp'],nb,st,mean,mg,'OK' if ok else 'BROKEN'))
print("\nTarget for a daily injectable: >1 mg/mL")
best=[r for r in rows if r[2]==0 and r[3]==0 and r[4]]
best.sort(key=lambda r:-r[1])
print("\nValid (no basic N, no stereocentre, warhead intact), best first:")
for n,mg,nb,st,ok,lp in best[:5]:
    print("   %-26s %8.4f mg/mL   cLogP %.2f   (%.0fx vs M3)"%(n,mg,lp,mg/[r[1] for r in rows if r[0]=='M3 (current)'][0]))

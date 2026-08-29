# -*- coding: utf-8 -*-
"""Prodrug design. Mask the polar groups so the molecule ENTERS the cell as a greasy
species; intracellular esterases cleave the caps and release the polar active form,
which is then TRAPPED inside by the very polarity that blocked entry.

Target window, from six GPX4 inhibitors that demonstrably kill cells:
   TPSA <= 93 A^2, HBD <= 1, cLogP roughly 3.4-4.8"""
from rdkit import Chem, RDLogger
from rdkit.Chem import rdMolDescriptors as rd, Crippen, Descriptors
RDLogger.DisableLog('rdApp.*')
TAIL='cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1'
def s1_ester(cap):
    """cap = acyl written left-to-right, e.g. 'CC(=O)' for acetate; '' = free alcohol"""
    left  = ('%sOCCNC(=O)'%cap) if cap else 'OCCNC(=O)'
    right = ('C(=O)NCCO%s'%cap[::-1].replace(')=(','')) if cap else 'C(=O)NCCO'
    return None
# explicit is safer than clever - write each one out
SER={
 'S1 (free, active form)' :'OCCNC(=O)c1ccc(C(c2ccc(C(=O)NCCO)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'P1 diacetate'           :'CC(=O)OCCNC(=O)c1ccc(C(c2ccc(C(=O)NCCOC(C)=O)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'P2 dipropionate'        :'CCC(=O)OCCNC(=O)c1ccc(C(c2ccc(C(=O)NCCOC(=O)CC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'P3 diisobutyrate'       :'CC(C)C(=O)OCCNC(=O)c1ccc(C(c2ccc(C(=O)NCCOC(=O)C(C)C)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'P4 dipivalate'          :'CC(C)(C)C(=O)OCCNC(=O)c1ccc(C(c2ccc(C(=O)NCCOC(=O)C(C)(C)C)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'P5 dihexanoate'         :'CCCCCC(=O)OCCNC(=O)c1ccc(C(c2ccc(C(=O)NCCOC(=O)CCCCC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
 'P6 dibenzoate'          :'O=C(OCCNC(=O)c1ccc(C(c2ccc(C(=O)NCCOC(=O)c3ccccc3)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1)c1ccccc1',
 '--- for reference ---'  :None,
 'ML210 (known active)'   :'O=C(N1CCN(C(c2ccc(Cl)cc2)c2ccc(Cl)cc2)CC1)c1noc(C)c1[N+](=O)[O-]',
 'GPX4-M3 (current lead)' :'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
}
wh=Chem.MolFromSmarts('c1noc(C)c1[N+](=O)[O-]')
est=Chem.MolFromSmarts('[CX3](=O)O[CX4]')
print("PRODRUG SERIES — ester caps on the two hydroxyls of GPX4-S1\n")
print("window from known cell-active GPX4 inhibitors: TPSA<=93, HBD<=1, cLogP 3.4-4.8\n")
print("%-24s %7s %7s %5s %7s %6s %7s  %s"%("compound","MW","TPSA","HBD","cLogP","esters","warhead","verdict"))
print("-"*92)
for n,s in SER.items():
    if s is None: print("%-24s"%n); continue
    m=Chem.MolFromSmiles(s)
    if m is None: print("  %-24s INVALID"%n); continue
    t=rd.CalcTPSA(m); lp=Crippen.MolLogP(m); hbd=rd.CalcNumHBD(m); mw=Descriptors.MolWt(m)
    ne=len(m.GetSubstructMatches(est)); ok=m.HasSubstructMatch(wh)
    if t<=93 and hbd<=1 and 3.0<=lp<=5.2: v='IN WINDOW'
    elif t<=115 and hbd<=1 and lp>=2.5:   v='close'
    else:                                  v='outside'
    print("%-24s %7.1f %7.1f %5d %7.2f %6d %7s  %s"%(n,mw,t,hbd,lp,ne,'OK' if ok else 'BROKEN',v))

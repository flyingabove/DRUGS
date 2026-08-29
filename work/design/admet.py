# -*- coding: utf-8 -*-
"""Tier 4 - ADMET. hERG pharmacophore, CYP soft spots, solubility, PPB, reactive-metabolite alerts."""
from rdkit import Chem, RDLogger
from rdkit.Chem import Descriptors, rdMolDescriptors as rd, Crippen
RDLogger.DisableLog('rdApp.*')
C={
'GPX4-M1 (piperazine)':'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2CCN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
'GPX4-M3 (2-oxopiperazine)':'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
'GPX4-M4 (piperidine)':'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)C2CCN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
'ML210 (reference)':'O=C(N1CCN(C(c2ccc(Cl)cc2)c2ccc(Cl)cc2)CC1)c1noc(C)c1[N+](=O)[O-]',
}
basic=Chem.MolFromSmarts("[NX3;H0,H1,H2;!$(N[C,S]=[O,S,N]);!$(N[a]);!$(N[N,O]);!$(N#*)]")
SOFT=[("benzylic/benzhydryl CH","[CX4H1,CX4H2]([c])[c]"),
      ("N-methyl amide (N-dealkyl)","[CH3][NX3][CX3]=O"),
      ("para-unsubstituted phenyl","[cH1]1[cH1][cH1][cH1][cH1][c]1"),
      ("aryl-Cl (dehalogenation)","[c][Cl]"),
      ("aliphatic ring CH2 alpha to N","[CH2]-[NX3]")]
RXN=[("aniline / arylamine (idiosyncratic tox)","[NX3H2,NX3H1][c]"),
     ("nitroaromatic (nitroreduction)","[c][N+](=O)[O-]"),
     ("Michael acceptor","[CX3]=[CX3][CX3]=O"),
     ("alkyl halide","[CX4][Cl,Br,I]")]
def esol(m):
    ap=sum(1 for a in m.GetAtoms() if a.GetIsAromatic())/max(1,m.GetNumHeavyAtoms())
    return 0.16-0.63*Crippen.MolLogP(m)-0.0062*Descriptors.MolWt(m)+0.066*rd.CalcNumRotatableBonds(m)-0.74*ap
print("TIER 4 — ADMET PANEL\n")
print("%-28s %7s %7s %7s %7s %8s %9s"%("compound","cLogP","logS","TPSA","basicN","hERG","PPB est"))
print("-"*80)
rows={}
for n,s in C.items():
    m=Chem.MolFromSmiles(s); lp=Crippen.MolLogP(m); nb=len(m.GetSubstructMatches(basic))
    ar=rd.CalcNumAromaticRings(m); ls=esol(m)
    # hERG pharmacophore: protonatable basic N + >=2 aromatic/hydrophobic centres + logP
    herg = (nb>0)*2 + (ar>=2)*1 + (lp>3.5)*1
    lab={0:"low",1:"low",2:"moderate",3:"MODERATE-HIGH",4:"HIGH"}[min(herg,4)]
    ppb = min(99.5, 40+18*max(lp,0))   # crude logP-driven binding estimate
    rows[n]=dict(lp=lp,ls=ls,nb=nb,herg=lab,ppb=ppb)
    print("%-28s %7.2f %7.2f %7.1f %7d %8s %8.0f%%"%(n,lp,ls,rd.CalcTPSA(m),nb,lab,ppb))
print("\n\nCYP METABOLIC SOFT SPOTS (sites likely to be oxidised)")
print("-"*80)
for n,s in C.items():
    m=Chem.MolFromSmiles(s); hits=[(lab,len(m.GetSubstructMatches(Chem.MolFromSmarts(sm)))) for lab,sm in SOFT]
    hits=[(l,c) for l,c in hits if c]
    print("  %-28s %s"%(n,", ".join("%s x%d"%(l,c) for l,c in hits) or "none flagged"))
print("\n\nREACTIVE-METABOLITE / TOX ALERTS")
print("-"*80)
for n,s in C.items():
    m=Chem.MolFromSmiles(s); hits=[l for l,sm in RXN if m.HasSubstructMatch(Chem.MolFromSmarts(sm))]
    print("  %-28s %s"%(n,", ".join(hits) or "none"))
print("""
NOTE on the nitroaromatic flag: it fires on ALL FOUR compounds including ML210,
because it IS the warhead. Rule 9 - an alert firing on the shared scaffold of a
validated chemotype is not a differentiator. It is a real class liability
(nitroreduction to arylamine), and it is inherited, not introduced by us.""")

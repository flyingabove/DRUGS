# -*- coding: utf-8 -*-
"""Tier 4.3 - consensus aqueous solubility. One empirical model is not evidence;
four disagreeing models at least bound the answer."""
from rdkit import Chem, RDLogger
from rdkit.Chem import Descriptors, rdMolDescriptors as rd, Crippen
RDLogger.DisableLog('rdApp.*')
C={'GPX4-M1':'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2CCN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
   'GPX4-M3':'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
   'GPX4-M4':'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)C2CCN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
   'ML210'  :'O=C(N1CCN(C(c2ccc(Cl)cc2)c2ccc(Cl)cc2)CC1)c1noc(C)c1[N+](=O)[O-]',
   'ref: caffeine (sol)':'Cn1cnc2c1c(=O)n(C)c(=O)n2C',
   'ref: griseofulvin (poor)':'COC1=CC(=O)C[C@@H](C)[C@@]11C(=O)c2c(O1)c(C)c(Cl)c(OC)c2OC'}
def props(m):
    return dict(mw=Descriptors.MolWt(m), lp=Crippen.MolLogP(m), tpsa=rd.CalcTPSA(m),
                rb=rd.CalcNumRotatableBonds(m), ar=rd.CalcNumAromaticRings(m),
                hbd=rd.CalcNumHBD(m), hba=rd.CalcNumHBA(m),
                ap=sum(1 for a in m.GetAtoms() if a.GetIsAromatic())/max(1,m.GetNumHeavyAtoms()))
def esol(p):   # Delaney 2004
    return 0.16-0.63*p['lp']-0.0062*p['mw']+0.066*p['rb']-0.74*p['ap']
def ali(p):    # Ali et al. 2012
    return -1.0374-1.0116*p['lp']+0.0080*p['tpsa']-0.0102*p['mw']+0.4373
def gse(p, mp):  # General Solubility Equation (Jain & Yalkowsky)
    return 0.5-0.01*(mp-25.0)-p['lp']
def mp_est(p):
    """Crude melting-point proxy. Rigid, symmetric, high-HBD aromatics pack well and
    melt high, which is exactly what suppresses solubility - the risk for M1/M3."""
    return 25+40*p['ar']+18*p['hbd']+0.25*p['tpsa']-12*p['rb']
print("TIER 4.3 - CONSENSUS AQUEOUS SOLUBILITY (logS, mol/L)\n")
print("%-26s %7s %7s %7s %7s %8s %10s"%("compound","ESOL","Ali","GSE","mean","MP est C","mg/mL @mean"))
print("-"*82)
for n,s in C.items():
    m=Chem.MolFromSmiles(s); p=props(m); mp=mp_est(p)
    vals=[esol(p),ali(p),gse(p,mp)]
    mean=sum(vals)/3
    mgml=(10**mean)*p['mw']*1000/1000
    print("%-26s %7.2f %7.2f %7.2f %7.2f %8.0f %10.3f"%(n,vals[0],vals[1],vals[2],mean,mp,mgml))
print("""
INTERPRETATION
  Reference anchors: caffeine is freely soluble (~21 mg/mL measured); griseofulvin is
  a classic poorly-soluble drug (~0.009 mg/mL measured). If the models place our
  compounds between those, the estimate is behaving.

  For a DAILY INJECTABLE the practical bar is roughly >1 mg/mL in a formulable
  vehicle; below ~0.1 mg/mL needs co-solvent/cyclodextrin/nanosuspension work.

  The melting-point term is the weak link: symmetric rigid molecules pack efficiently
  and melt high, which is exactly the liability our symmetry choice creates. That
  cannot be settled computationally - it needs a measured melting point.""")

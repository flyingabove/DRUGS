# -*- coding: utf-8 -*-
"""The target enzyme is INSIDE the cell. The drug must cross a membrane to reach it.
Solubility optimisation pushes polarity UP; membrane crossing wants it DOWN.
Have I been trading away the ability to get in?"""
from rdkit import Chem, RDLogger
from rdkit.Chem import Descriptors, rdMolDescriptors as rd, Crippen
RDLogger.DisableLog('rdApp.*')
C={'ML210 (works in cells)':'O=C(N1CCN(C(c2ccc(Cl)cc2)c2ccc(Cl)cc2)CC1)c1noc(C)c1[N+](=O)[O-]',
   'GPX4-M1':'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2CCN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
   'GPX4-M3 (lead)':'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
   'GPX4-S3':'NC(=O)c1ccc(C(c2ccc(C(=O)N)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
   'GPX4-S4':'CNS(=O)(=O)c1ccc(C(c2ccc(S(=O)(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',
   'GPX4-S1 (most soluble)':'OCCNC(=O)c1ccc(C(c2ccc(C(=O)NCCO)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1'}
print("CAN IT GET INSIDE THE CELL?  (the target enzyme is intracellular)\n")
print("%-24s %7s %6s %5s %5s %9s  %s"%("compound","TPSA","cLogP","HBD","HBA","logP-TPSA","passive permeability"))
print("-"*94)
for n,s in C.items():
    m=Chem.MolFromSmiles(s)
    t=rd.CalcTPSA(m); lp=Crippen.MolLogP(m); hbd=rd.CalcNumHBD(m); hba=rd.CalcNumHBA(m)
    # widely used heuristics: TPSA<140 good, >140 poor for passive diffusion;
    # HBD<=5; a rough permeability index combining both
    idx=lp-0.01*t
    if t<=90 and hbd<=3: verd="good"
    elif t<=140 and hbd<=4: verd="moderate"
    elif t<=180: verd="POOR"
    else: verd="VERY POOR"
    print("%-24s %7.1f %6.2f %5d %5d %9.2f  %s"%(n,t,lp,hbd,hba,idx,verd))
print("""
  Rule of thumb: polar surface area (TPSA) above ~140 A^2 makes passive membrane
  crossing hard; above ~180 it is generally very hard. Hydrogen-bond donors cost
  extra because each one must be stripped of water to enter the membrane.

  ML210 - the compound known to kill cells - sits at 92.7. Every molecule in this
  series is well above it, and the solubility work pushed further in that direction.""")

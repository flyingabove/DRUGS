# -*- coding: utf-8 -*-
"""IS THE 93 A^2 CEILING REAL, OR AN ARTIFACT OF A SMALL CHEMOTYPE SET?

The ceiling came from six GPX4 inhibitors - one chemical series. If APPROVED covalent
drugs with INTRACELLULAR targets routinely exceed it, the constraint is far softer
than assumed and GPX4-M3 may be viable after all.

Each SMILES is checked against its published molecular weight. That is necessary but
NOT sufficient (a ring-digit collision preserves MW) - so mismatches are flagged loudly
and treated as unusable rather than quietly averaged in."""
from rdkit import Chem, RDLogger
from rdkit.Chem import rdMolDescriptors as rd, Crippen, Descriptors
RDLogger.DisableLog('rdApp.*')

# approved covalent drugs whose target is INSIDE the cell, with published MW
COV={
 'ibrutinib (BTK)'      :('C=CC(=O)N1CCC[C@@H](C1)n1nc(-c2ccc(Oc3ccccc3)cc2)c2c(N)ncnc21',440.5),
 'acalabrutinib (BTK)'  :('CC#CC(=O)N1CCC[C@H]1c1nc(-c2ccc(C(=O)Nc3ccccn3)cc2)c2c(N)nccn12',465.5),
 'osimertinib (EGFR)'   :('C=CC(=O)Nc1cc(Nc2nccc(-c3cn(C)c4ccccc34)n2)c(OC)cc1N(C)CCN(C)C',499.6),
 'afatinib (EGFR)'      :('CN(C)C/C=C/C(=O)Nc1cc2c(Nc3ccc(F)c(Cl)c3)ncnc2cc1O[C@H]1CCOC1',485.9),
 'neratinib (EGFR)'     :('CCOc1cc2ncc(C#N)c(Nc3ccc(OCc4ccccn4)c(Cl)c3)c2cc1NC(=O)/C=C/CN(C)C',557.0),
 'sotorasib (KRAS)'     :('CC(C)c1cc(C(=O)N2CCN(C(=O)C=C)C[C@H]2C)c2c(n1)c(-c1c(C)ccc(O)c1F)nn2C',560.6),
 'bortezomib (20S)'     :('CC(C)C[C@@H](NC(=O)[C@@H](Cc1ccccc1)NC(=O)c1cnccn1)B(O)O',384.2),
 'nirmatrelvir (Mpro)'  :('CC1(C)[C@@H]2[C@H]1[C@H](C(=O)NC(CC1CCNC1=O)C#N)N(C(=O)[C@@H](NC(=O)C(F)(F)F)C(C)(C)C)C2',499.5),
}
NONCOV_REF={
 'ML210 (our parent)'   :('O=C(N1CCN(C(c2ccc(Cl)cc2)c2ccc(Cl)cc2)CC1)c1noc(C)c1[N+](=O)[O-]',475.3),
}
OURS={
 'GPX4-C1 (new lead)'   :('O=C(N1CCN(C(c2ccccc2)c3ccccc3)CC1)c5noc(C)c5[N+](=O)[O-]',406.4),
 'GPX4-M3 (deprioritised)':('CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',534.5),
 'GPX4-S1'              :('OCCNC(=O)c1ccc(C(c2ccc(C(=O)NCCO)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1',594.6),
}
def check(name,smi,mw_pub):
    m=Chem.MolFromSmiles(smi)
    if m is None: return None,'PARSE FAILED'
    mw=Descriptors.MolWt(m)
    if abs(mw-mw_pub)>1.5: return None,'MW %.1f vs published %.1f - SMILES WRONG'%(mw,mw_pub)
    return m,None
print("IS THE CEILING REAL?  Approved covalent drugs with intracellular targets\n")
print("%-26s %7s %7s %5s %7s  %s"%("drug","MW","TPSA","HBD","cLogP","note"))
print("-"*74)
vals=[]
for n,(s,mwp) in COV.items():
    m,err=check(n,s,mwp)
    if err: print("%-26s  --  %s"%(n,err)); continue
    t=rd.CalcTPSA(m); vals.append((n,t))
    print("%-26s %7.1f %7.1f %5d %7.2f"%(n,Descriptors.MolWt(m),t,rd.CalcNumHBD(m),Crippen.MolLogP(m)))
print()
for grp,d in [('reference',NONCOV_REF),('ours',OURS)]:
    for n,(s,mwp) in d.items():
        m,err=check(n,s,mwp)
        if err: print("%-26s  --  %s"%(n,err)); continue
        print("%-26s %7.1f %7.1f %5d %7.2f  <- %s"%(n,Descriptors.MolWt(m),rd.CalcTPSA(m),
              rd.CalcNumHBD(m),Crippen.MolLogP(m),grp))
if vals:
    ts=[t for _,t in vals]
    print("\n  approved covalent, intracellular: TPSA range %.1f - %.1f, median %.1f"%(min(ts),max(ts),sorted(ts)[len(ts)//2]))
    print("  highest: %s"%max(vals,key=lambda x:x[1])[0])
    print("\n  the GPX4-only ceiling was 92.7. Compounds above it: %d/%d"%(sum(1 for t in ts if t>92.7),len(ts)))

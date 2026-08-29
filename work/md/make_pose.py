# -*- coding: utf-8 -*-
"""Build the MD ligand BY EDITING the posed adduct, so coordinates are preserved exactly.
Aligning a freshly embedded conformer gave 2.0 A RMSD - a different conformer, not a
different pose. Editing avoids the problem entirely."""
import numpy as np
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem
from rdkit.Geometry import Point3D
RDLogger.DisableLog('rdApp.*')

POSE_SMI = 'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)C(=N[O-])[Se]C)CC2)cc1'
X  = np.load('../qmcluster/m3_pose_full.npy')
EL = open('../qmcluster/m3_pose_elements.txt').read().split()

pose = Chem.AddHs(Chem.MolFromSmiles(POSE_SMI))
assert pose.GetNumAtoms() == len(X)
conf = Chem.Conformer(pose.GetNumAtoms())
for i, p in enumerate(X):
    conf.SetAtomPosition(i, Point3D(*[float(v) for v in p]))
pose.AddConformer(conf, assignId=True)

se = [a.GetIdx() for a in pose.GetAtoms() if a.GetSymbol() == 'Se'][0]
se_pos = np.array(X[se])
# atoms to delete: Se, its methyl C, and that methyl's hydrogens
nbrs = [n.GetIdx() for n in pose.GetAtomWithIdx(se).GetNeighbors()]
def heavy_deg(idx):
    return sum(1 for n in pose.GetAtomWithIdx(idx).GetNeighbors() if n.GetSymbol() != 'H')
# the methyl carbon has ONE heavy neighbour (Se); the attachment carbon has several.
# Plain GetDegree() cannot tell them apart once hydrogens are explicit.
attach = [i for i in nbrs if heavy_deg(i) > 1]
me = [i for i in nbrs if heavy_deg(i) == 1]
assert len(attach) == 1 and len(me) == 1, (attach, me)
attach, me = attach[0], me[0]
kill = {se, me} | {n.GetIdx() for n in pose.GetAtomWithIdx(me).GetNeighbors()
                   if n.GetSymbol() == 'H'}
print('deleting Se(%d), methyl C(%d) + %d H' % (se, me, len(kill) - 2))

rw = Chem.RWMol(pose)
# neutralise the oximate O- -> OH (neutral oxime, the form present at pH 7.4)
for a in rw.GetAtoms():
    if a.GetSymbol() == 'O' and a.GetFormalCharge() == -1:
        a.SetFormalCharge(0); a.SetNoImplicit(False); a.SetNumExplicitHs(1)
for i in sorted(kill, reverse=True):
    rw.RemoveAtom(i)
md = rw.GetMol()
Chem.SanitizeMol(md)
md = Chem.AddHs(md, addCoords=True)
print('MD ligand: %d atoms  radicals=%d  chg%+d' % (
    md.GetNumAtoms(), sum(a.GetNumRadicalElectrons() for a in md.GetAtoms()),
    Chem.GetFormalCharge(md)))
print('SMILES:', Chem.MolToSmiles(Chem.RemoveHs(md)))

P = md.GetConformer().GetPositions()
np.save('m3_pose.npy', P)
Chem.MolToMolFile(md, 'm3_lig.sdf')
d = np.linalg.norm(P - se_pos, axis=1)
print('-> m3_pose.npy (%d atoms). Closest atom to former Se: %.2f A (atom %d, %s)'
      % (len(P), d.min(), int(d.argmin()), md.GetAtomWithIdx(int(d.argmin())).GetSymbol()))

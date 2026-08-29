# -*- coding: utf-8 -*-
"""Tier 2.4 — does the modified region stay solvent-facing once the protein moves?

Every burial number so far came from a RIGID receptor. This is the test that retires
that caveat. Rule 23: print the tables, interpret in the document.
"""
import json, sys
import numpy as np
import mdtraj as md

meta = json.load(open('md_meta.json'))
LIG0, NLIG = meta['lig_start'], meta['n_lig']
SG, ATTACH = meta['sg'], meta['attach']

# A DCD being actively written cannot be opened - OpenMM rewrites the header on each
# flush, so mdtraj hits "premature end of file". Copy first, read the copy. This also
# makes partial-trajectory analysis possible while the run continues.
import shutil
shutil.copy('traj.dcd', 'snap.dcd')
t = md.load('snap.dcd', top='equil.pdb')
print('trajectory: %d frames, %d atoms, %.1f ns'
      % (t.n_frames, t.n_atoms, t.time[-1] / 1000.0 if t.n_frames > 1 else 0))
t = t.superpose(t, 0, atom_indices=t.topology.select('protein and name CA'))

lig = list(range(LIG0, LIG0 + NLIG))
heavy = [i for i in lig if t.topology.atom(i).element.symbol != 'H']

# --- 1. did the tether hold?
d = md.compute_distances(t, np.array([[SG, ATTACH]])) * 10.0
print('\nTETHER  Cys46 SG - ligand C:  mean %.2f A  sd %.2f  range %.2f-%.2f'
      % (d.mean(), d.std(), d.min(), d.max()))

# --- 2. per-atom SASA of the ligand, and specifically the modified arms
sasa = md.shrake_rupley(t, mode='atom')            # nm^2
lig_sasa = sasa[:, heavy] * 100.0                  # -> A^2

# the N-methylamide arms: C(=O)N(H)CH3 groups on the two aryl rings
top = t.topology
arms = []
for a in lig:
    at = top.atom(a)
    if at.element.symbol == 'N':
        nbrs = [b for b in top.bonds if a in (b[0].index, b[1].index)]
        syms = []
        for b in nbrs:
            o = b[1] if b[0].index == a else b[0]
            syms.append(o.element.symbol)
        if syms.count('C') >= 2 and 'H' in syms:
            arms.append(a)
print('amide N atoms identified in ligand: %s' % arms)

print('\nLIGAND SOLVENT EXPOSURE OVER THE TRAJECTORY')
print('  whole ligand   mean SASA %.1f A^2  (sd %.1f)'
      % (lig_sasa.sum(axis=1).mean(), lig_sasa.sum(axis=1).std()))
if arms:
    arm_idx = [heavy.index(a) for a in arms if a in heavy]
    arm_sasa = lig_sasa[:, arm_idx].sum(axis=1)
    print('  amide arms     mean SASA %.1f A^2  (sd %.1f)  min %.1f'
          % (arm_sasa.mean(), arm_sasa.std(), arm_sasa.min()))
    print('  frames where the arms are fully buried (SASA < 1 A^2): %d / %d'
          % (int((arm_sasa < 1.0).sum()), t.n_frames))

# --- 3. per-atom mean burial, ranked
print('\nPER-ATOM MEAN SASA (A^2), ligand heavy atoms, lowest 6 and highest 6:')
mean_at = lig_sasa.mean(axis=0)
order = np.argsort(mean_at)
for lbl, idx in [('most buried ', order[:6]), ('most exposed', order[-6:])]:
    print('  %s: %s' % (lbl, ', '.join(
        '%s%d %.1f' % (top.atom(heavy[i]).element.symbol, heavy[i], mean_at[i])
        for i in idx)))

# --- 4. protein stability check: did the fold survive?
ca = t.topology.select('protein and name CA')
rmsd = md.rmsd(t, t, 0, atom_indices=ca) * 10.0
print('\nPROTEIN Ca RMSD vs frame 0: mean %.2f A  final %.2f A  max %.2f A'
      % (rmsd.mean(), rmsd[-1], rmsd.max()))

json.dump({'n_frames': int(t.n_frames),
           'tether_mean': float(d.mean()), 'tether_sd': float(d.std()),
           'lig_sasa_mean': float(lig_sasa.sum(axis=1).mean()),
           'arm_sasa_mean': float(arm_sasa.mean()) if arms else None,
           'ca_rmsd_mean': float(rmsd.mean()), 'ca_rmsd_final': float(rmsd[-1])},
          open('md_analysis.json', 'w'), indent=1)
print('\n-> md_analysis.json')

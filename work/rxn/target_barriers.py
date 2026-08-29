# -*- coding: utf-8 -*-
"""TIER 1 TARGET — selenolate vs thiolate attacking the unmasked nitrile oxide.

This is the actual selectivity number: ddG++ (Cys - Se). Run ONLY after the SN2
control in barriers.py has reproduced the known relative nucleophilicity, otherwise
the protocol is unvalidated and the number is worthless (Rule 12/20).

Same protocol as the control: HF/def2-SVP geometry in Cartesian coordinates, frozen
Nu...C distance, wb97x-d/def2-SVPD + IEFPCM single point.
"""
import json
import numpy as np
import psi4
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem

RDLogger.DisableLog('rdApp.*')
H2K = 627.5094740631
Z = {'H': 1, 'C': 6, 'N': 7, 'O': 8, 'S': 16, 'Se': 34, 'Br': 35}

psi4.set_memory('3000 MB')
psi4.core.set_output_file('psi4_target.log', False)
psi4.set_num_threads(3)
psi4.set_options({'reference': 'rks', 'scf_type': 'df', 'g_convergence': 'gau_loose',
                  'geom_maxiter': 60, 'guess': 'sad', 'maxiter': 200})

OPT = 'hf/def2-svp'
SP = 'wb97x-d/def2-svpd'
PCM_INPUT = ('units = angstrom\nmedium {\n  solvertype = iefpcm\n  solvent = water\n}\n'
             'cavity {\n  radiiset = bondi\n  type = gepol\n  area = 0.4\n}\n')

ELEC = 'CN(C)C(=O)C#[N+][O-]'      # unmasked ML210-type acyl nitrile oxide


def mol(S, P, chrg):
    ne = sum(Z[s] for s in S) - chrg
    assert ne % 2 == 0, 'odd electron count %d - singlet impossible' % ne
    lines = ['%d 1' % chrg]
    lines += ['%s %.8f %.8f %.8f' % (s, p[0], p[1], p[2]) for s, p in zip(S, P)]
    lines += ['units angstrom', 'no_reorient', 'no_com']
    return psi4.geometry('\n'.join(lines))


def build(nu_sym, r0=3.40):
    """Nucleophile attacks the nitrile-oxide carbon where an sp2 substituent would go."""
    m = Chem.AddHs(Chem.MolFromSmiles(ELEC))
    AllChem.EmbedMolecule(m, randomSeed=11)
    AllChem.MMFFOptimizeMolecule(m)
    P = m.GetConformer().GetPositions()
    S = [a.GetSymbol() for a in m.GetAtoms()]
    ci = ni = None
    for b in m.GetBonds():
        if b.GetBondType() == Chem.BondType.TRIPLE:
            a1, a2 = b.GetBeginAtom(), b.GetEndAtom()
            if {a1.GetSymbol(), a2.GetSymbol()} == {'C', 'N'}:
                ci = a1.GetIdx() if a1.GetSymbol() == 'C' else a2.GetIdx()
                ni = a2.GetIdx() if a1.GetSymbol() == 'C' else a1.GetIdx()
    assert ci is not None, 'nitrile oxide carbon not found'
    ri = [n.GetIdx() for n in m.GetAtomWithIdx(ci).GetNeighbors() if n.GetIdx() != ni][0]
    u1 = P[ri] - P[ci]; u1 /= np.linalg.norm(u1)
    u2 = P[ni] - P[ci]; u2 /= np.linalg.norm(u2)
    d = -(u1 + u2); d /= np.linalg.norm(d)
    nu = P[ci] + d * r0
    me = nu + d * 1.95
    hs = [me + np.array([0.62, 0.62, 0.0]), me + np.array([-0.62, 0.62, 0.31]),
          me + np.array([0.0, -0.85, -0.52])]
    S2 = S + [nu_sym, 'C', 'H', 'H', 'H']
    P2 = np.vstack([P, nu, me] + hs)
    return S2, P2, ci, len(S), len(S)      # i_c, i_nu, nu_from


def scan(tag, S, P0, chrg, i_c, i_nu, dists, nu_from):
    res = []
    for d in dists:
        cur = np.array(P0, dtype=float)
        v = cur[i_nu] - cur[i_c]; v /= np.linalg.norm(v)
        cur[nu_from:] += (d - np.linalg.norm(cur[i_nu] - cur[i_c])) * v
        m = mol(S, cur, chrg)
        psi4.set_options({'pcm': False,
                          'optking__frozen_distance': '%d %d' % (i_c + 1, i_nu + 1),
                          'optking__opt_coordinates': 'cartesian',
                          'optking__intrafrag_step_limit': 0.2})
        ok = True
        try:
            psi4.optimize(OPT, molecule=m)
        except Exception as e:
            ok = False
            print('    [%s d=%.2f] opt failed (%s)' % (tag, d, type(e).__name__), flush=True)
            m = mol(S, cur, chrg)
        psi4.set_options({'pcm': True, 'pcm_scf_type': 'total'})
        psi4.pcm_helper(PCM_INPUT)
        try:
            e = float(psi4.energy(SP, molecule=m))
        except Exception as ex:
            print('    [%s d=%.2f] ENERGY FAILED (%s)' % (tag, d, type(ex).__name__), flush=True)
            e = float('nan')
        psi4.set_options({'pcm': False})
        psi4.core.clean()
        res.append((float(d), e))
        print('    %-8s d=%.2f  E=%.8f %s' % (tag, d, e, '' if ok else '(unrelaxed)'), flush=True)
    return res


def summarise(res):
    d = np.array([a for a, _ in res]); E = np.array([b for _, b in res])
    rel = (E - E[0]) * H2K
    nbad = int(np.isnan(E).sum())
    if nbad:
        print('    WARNING: %d/%d points failed - barrier NOT reported' % (nbad, len(E)))
        return dict(d=d.tolist(), rel=rel.tolist(), barrier=float('nan'), failed=nbad)
    i = int(np.argmax(rel))
    return dict(d=d.tolist(), rel=rel.tolist(), barrier=float(rel[i]),
                d_ts=float(d[i]), dE=float(rel[-1]), failed=0)


def main():
    DIST = [3.4, 3.0, 2.7, 2.45, 2.25, 2.1, 1.95]
    out = {}
    print('=== TARGET: acyl nitrile oxide + CH3Nu(-) -> adduct ===\n', flush=True)
    for nu in ['Se', 'S']:
        S, P, i_c, i_nu, frm = build(nu)
        out['tgt_' + nu] = summarise(scan('tgt-' + nu, S, P, -1, i_c, i_nu, DIST, frm))
        print('  --> %s barrier %.2f kcal/mol\n' % (nu, out['tgt_' + nu]['barrier']), flush=True)
    a, b = out['tgt_Se']['barrier'], out['tgt_S']['barrier']
    print('  ddG++ (Cys - Se) = %+.2f kcal/mol' % (b - a))
    print('  kill criterion: > 2 kcal/mol favouring Se')
    print('  %s' % ('PASS' if (b - a) > 2 else ('FAIL - promiscuous alkylator risk'
                                                if (b - a) < 0.5 else 'MARGINAL')))
    json.dump(out, open('target_barrier_results.json', 'w'), indent=1)
    print('\n-> target_barrier_results.json', flush=True)


if __name__ == '__main__':
    main()

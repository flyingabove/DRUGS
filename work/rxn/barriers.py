# -*- coding: utf-8 -*-
"""TIER 1 — BARRIERS. The quantity selectivity actually depends on.

Rule 20: the control must match the CLAIM's quantity. "Selenolate is the better
nucleophile" is about the BARRIER. The first Tier 1 pass computed reaction ENERGIES
and mis-diagnosed two methods as a result.

Protocol: relaxed scan along d(Nu...C). Geometry optimisation in GAS PHASE (psi4 has
no analytic PCM gradients and silently falls back to finite differences, which is
intractable), IEFPCM single point at every scan point.
"""
import sys, json
import numpy as np
import psi4

H2K = 627.5094740631
Z = {'H': 1, 'C': 6, 'N': 7, 'O': 8, 'S': 16, 'Se': 34, 'Br': 35}

psi4.set_memory('3000 MB')
psi4.core.set_output_file('psi4_barrier.log', False)
psi4.set_num_threads(4)
psi4.set_options({'reference': 'rks', 'scf_type': 'df',
                  'g_convergence': 'gau_loose', 'geom_maxiter': 60,
                  'guess': 'sad', 'maxiter': 200})

OPT = 'wb97x-d/def2-svpd'
SP = 'wb97x-d/def2-tzvppd'
PCM_INPUT = ('units = angstrom\nmedium {\n  solvertype = iefpcm\n  solvent = water\n}\n'
             'cavity {\n  radiiset = bondi\n  type = gepol\n  area = 0.4\n}\n')


def mol(S, P, chrg):
    """Build a psi4 molecule, asserting the electron count permits a singlet.

    A 'chg/mult inconsistent' error from psi4 usually means an IMPOSSIBLE ELECTRON
    COUNT, not a parser problem. Checking here turns a confusing downstream error
    into an immediate, readable one.
    """
    ne = sum(Z[s] for s in S) - chrg
    assert ne % 2 == 0, ('odd electron count %d - singlet impossible; the molecule '
                         'is mis-specified' % ne)
    lines = ['%d 1' % chrg]
    lines += ['%s %.8f %.8f %.8f' % (s, p[0], p[1], p[2]) for s, p in zip(S, P)]
    lines += ['units angstrom', 'no_reorient', 'no_com']
    return psi4.geometry('\n'.join(lines))


def scan(tag, S, P0, chrg, i_c, i_nu, dists, nu_from):
    """i_c: electrophilic carbon. i_nu: nucleophile heavy atom.
    nu_from: first index of the nucleophile fragment (translated as a rigid block)."""
    res = []
    cur = np.array(P0, dtype=float)
    for d in dists:
        v = cur[i_nu] - cur[i_c]
        v = v / np.linalg.norm(v)
        cur = cur.copy()
        cur[nu_from:] += (d - np.linalg.norm(cur[i_nu] - cur[i_c])) * v
        m = mol(S, cur, chrg)
        psi4.set_options({'pcm': False,
                          'optking__frozen_distance': '%d %d' % (i_c + 1, i_nu + 1)})
        try:
            psi4.optimize(OPT, molecule=m)
            cur = m.geometry().to_array() * 0.52917721092
        except Exception as e:
            print('    [%s d=%.2f] opt issue: %s' % (tag, d, type(e).__name__))
        psi4.set_options({'pcm': True, 'pcm_scf_type': 'total'})
        psi4.pcm_helper(PCM_INPUT)
        try:
            e = float(psi4.energy(SP, molecule=m))
        except Exception:
            e = float('nan')
        psi4.set_options({'pcm': False})
        psi4.core.clean()
        res.append((float(d), e))
        print('    %-8s d=%.2f  E=%.8f' % (tag, d, e), flush=True)
    return res


def summarise(res):
    d = np.array([a for a, _ in res])
    E = np.array([b for _, b in res])
    rel = (E - E[0]) * H2K
    i = int(np.nanargmax(rel))
    return dict(d=d.tolist(), rel=rel.tolist(), barrier=float(rel[i]),
                d_ts=float(d[i]), dE=float(rel[-1]))


def sn2_geom(nu):
    """CH3Br + CH3Nu(-) collinear backside attack."""
    S = ['C', 'Br', 'H', 'H', 'H', nu, 'C', 'H', 'H', 'H']
    P = np.array([[0, 0, 0], [0, 0, 1.95],
                  [1.03, 0, -0.36], [-0.515, 0.891, -0.36], [-0.515, -0.891, -0.36],
                  [0, 0, -3.40], [0, 0, -5.30],
                  [1.03, 0, -5.66], [-0.515, 0.891, -5.66], [-0.515, -0.891, -5.66]],
                 dtype=float)
    return S, P, 0, 5, 5


def main():
    DIST = [3.4, 3.0, 2.7, 2.45, 2.25, 2.1, 1.95]
    out = {}
    print('=== KINETIC CONTROL: SN2  CH3Br + CH3Nu(-) -> CH3Nu-CH3 + Br(-) ===')
    print('    expectation: SELENOLATE HAS THE LOWER BARRIER\n', flush=True)
    for nu in ['Se', 'S']:
        S, P, i_c, i_nu, frm = sn2_geom(nu)
        out['ctl_' + nu] = summarise(scan('ctl-' + nu, S, P, -1, i_c, i_nu, DIST, frm))
        print('  --> %s barrier %.2f kcal/mol at d=%.2f\n'
              % (nu, out['ctl_' + nu]['barrier'], out['ctl_' + nu]['d_ts']), flush=True)
    dd = out['ctl_Se']['barrier'] - out['ctl_S']['barrier']
    print('  CONTROL  dE++(Se) - dE++(S) = %+.2f kcal/mol' % dd)
    print('  %s' % ('PASS - selenolate lower barrier, matches experiment' if dd < 0
                    else 'FAIL - does not reproduce known relative nucleophilicity'))
    json.dump(out, open('barrier_results.json', 'w'), indent=1)
    print('\n-> barrier_results.json', flush=True)


if __name__ == '__main__':
    main()

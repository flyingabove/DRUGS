# -*- coding: utf-8 -*-
"""TIER 1 BARRIERS v2 — two-bond reaction coordinate.

Why v1 failed (Rule 30): it froze only the FORMING bond d(C...Nu) and let the
BREAKING bond d(C-Br) relax freely. Each grid point was optimised independently, so
between d=2.45 and d=2.25 the optimiser fell into the product basin and the profile
jumped 46 kcal/mol in one 0.2 A step. The apparent "+23.6 barrier" was just the last
point before the surface snapped.

v2 walks BOTH bonds along a defined path and freezes BOTH at every point. The system
cannot hop basins because the breaking bond is no longer free to collapse.

Geometries are also CHAINED along the path (each point starts from the previous
optimised structure), which is what keeps a scan continuous. v1 rebuilt each point
from scratch to avoid propagating failures - that fixed error propagation and caused
basin-hopping instead.
"""
import json
import numpy as np
import psi4

H2K = 627.5094740631
Z = {'H': 1, 'C': 6, 'N': 7, 'O': 8, 'S': 16, 'Se': 34, 'Br': 35}

psi4.set_memory('3000 MB')
psi4.core.set_output_file('psi4_barrier2.log', False)
psi4.set_num_threads(3)
psi4.set_options({'reference': 'rks', 'scf_type': 'df', 'g_convergence': 'gau_loose',
                  'geom_maxiter': 70, 'guess': 'sad', 'maxiter': 200})

OPT = 'hf/def2-svp'
SP = 'wb97x-d/def2-svpd'
PCM_INPUT = ('units = angstrom\nmedium {\n  solvertype = iefpcm\n  solvent = water\n}\n'
             'cavity {\n  radiiset = bondi\n  type = gepol\n  area = 0.4\n}\n')

# path: forming bond shortens while breaking bond lengthens, monotonically
PATH = [(3.20, 1.98), (2.90, 2.02), (2.65, 2.08), (2.45, 2.16), (2.30, 2.26),
        (2.20, 2.38), (2.10, 2.52), (2.02, 2.70), (1.96, 2.95), (1.92, 3.25)]


def mol(S, P, chrg):
    ne = sum(Z[s] for s in S) - chrg
    assert ne % 2 == 0, 'odd electron count %d - singlet impossible' % ne
    lines = ['%d 1' % chrg]
    lines += ['%s %.8f %.8f %.8f' % (s, p[0], p[1], p[2]) for s, p in zip(S, P)]
    lines += ['units angstrom', 'no_reorient', 'no_com']
    return psi4.geometry('\n'.join(lines))


def sn2_geom(nu):
    S = ['C', 'Br', 'H', 'H', 'H', nu, 'C', 'H', 'H', 'H']
    P = np.array([[0, 0, 0], [0, 0, 1.98],
                  [1.03, 0, -0.36], [-0.515, 0.891, -0.36], [-0.515, -0.891, -0.36],
                  [0, 0, -3.20], [0, 0, -5.10],
                  [1.03, 0, -5.46], [-0.515, 0.891, -5.46], [-0.515, -0.891, -5.46]],
                 dtype=float)
    return S, P


def scan(tag, S, P0, chrg, i_c=0, i_lg=1, i_nu=5, nu_from=5):
    res = []
    cur = np.array(P0, dtype=float)
    for (d_form, d_break) in PATH:
        # set the forming bond by moving the nucleophile fragment along its axis
        v = cur[i_nu] - cur[i_c]; v /= np.linalg.norm(v)
        cur = cur.copy()
        cur[nu_from:] += (d_form - np.linalg.norm(cur[i_nu] - cur[i_c])) * v
        # set the breaking bond by moving the leaving group along its axis
        w = cur[i_lg] - cur[i_c]; w /= np.linalg.norm(w)
        cur[i_lg] += (d_break - np.linalg.norm(cur[i_lg] - cur[i_c])) * w
        m = mol(S, cur, chrg)
        psi4.set_options({
            'pcm': False,
            'optking__frozen_distance': '%d %d %d %d' % (i_c + 1, i_nu + 1, i_c + 1, i_lg + 1),
            'optking__opt_coordinates': 'cartesian',
            'optking__intrafrag_step_limit': 0.2})
        ok = True
        try:
            psi4.optimize(OPT, molecule=m)
            cur = m.geometry().to_array() * 0.52917721092     # CHAIN to next point
        except Exception as e:
            ok = False
            print('    [%s %.2f/%.2f] opt failed (%s)' % (tag, d_form, d_break,
                                                          type(e).__name__), flush=True)
            m = mol(S, cur, chrg)
        psi4.set_options({'pcm': True, 'pcm_scf_type': 'total'})
        psi4.pcm_helper(PCM_INPUT)
        try:
            e = float(psi4.energy(SP, molecule=m))
        except Exception as ex:
            print('    [%s] ENERGY FAILED (%s)' % (tag, type(ex).__name__), flush=True)
            e = float('nan')
        psi4.set_options({'pcm': False})
        psi4.core.clean()
        res.append((d_form, d_break, e, ok))
        print('    %-8s form=%.2f break=%.2f  E=%.8f %s'
              % (tag, d_form, d_break, e, '' if ok else '(unrelaxed)'), flush=True)
    return res


def summarise(tag, res):
    E = np.array([r[2] for r in res])
    rel = (E - E[0]) * H2K
    nbad = int(np.isnan(E).sum())
    if nbad:
        print('    WARNING: %d/%d points failed - no barrier reported' % (nbad, len(E)))
        return dict(barrier=float('nan'), failed=nbad, rel=rel.tolist())
    # Rule 30: a physical profile is smooth. Refuse to report across a discontinuity.
    jumps = np.abs(np.diff(rel))
    if jumps.max() > 15.0:
        i = int(np.argmax(jumps))
        print('    WARNING: discontinuity %.1f kcal/mol between points %d and %d '
              '- no barrier reported' % (jumps.max(), i, i + 1))
        return dict(barrier=float('nan'), discontinuity=float(jumps.max()),
                    rel=rel.tolist())
    i = int(np.argmax(rel))
    print('    profile smooth (max step %.1f kcal/mol)' % jumps.max())
    return dict(barrier=float(rel[i]), i_ts=i, max_step=float(jumps.max()),
                rel=rel.tolist(), failed=0)


def main():
    out = {}
    print('=== KINETIC CONTROL v2: two-bond coordinate ===')
    print('    expectation: SELENOLATE HAS THE LOWER BARRIER\n', flush=True)
    for nu in ['Se', 'S']:
        S, P = sn2_geom(nu)
        r = scan('ctl-' + nu, S, P, -1)
        out['ctl_' + nu] = summarise('ctl-' + nu, r)
        out['ctl_' + nu]['path'] = [(a, b) for a, b, _ in r]
        print('  --> %s barrier %s\n' % (nu, out['ctl_' + nu]['barrier']), flush=True)
    a, b = out['ctl_Se']['barrier'], out['ctl_S']['barrier']
    if np.isnan(a) or np.isnan(b):
        print('  CONTROL INVALID - one or both profiles unusable')
    else:
        print('  CONTROL  dE++(Se) - dE++(S) = %+.2f kcal/mol' % (a - b))
        print('  %s' % ('PASS - selenolate lower barrier' if a < b else
                        'FAIL - does not reproduce known nucleophilicity'))
    json.dump(out, open('barrier2_results.json', 'w'), indent=1)
    print('\n-> barrier2_results.json', flush=True)


if __name__ == '__main__':
    main()

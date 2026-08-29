# -*- coding: utf-8 -*-
"""TIER 1 BARRIERS v3 — one frozen bond, CHAINED geometries.

Why v1 failed (Rule 30): it froze only the FORMING bond d(C...Nu) and let the
BREAKING bond d(C-Br) relax freely. Each grid point was optimised independently, so
between d=2.45 and d=2.25 the optimiser fell into the product basin and the profile
jumped 46 kcal/mol in one 0.2 A step. The apparent "+23.6 barrier" was just the last
point before the surface snapped.

v2 froze BOTH bonds and chained geometries. That fixed the basin-hopping but
OVER-CONSTRAINED the system: optimisation failed at the two points nearest the
transition region and the profile inflated to +48 kcal/mol against an expected
~20-25 for an SN2 in water. Unrelaxed energies are upper bounds, not physics.

v3 isolates the variable that actually mattered. v1 froze ONE bond but rebuilt each
point from scratch (-> basin hop). v2 froze TWO bonds and chained (-> over-constrained).
v3 freezes ONE bond and CHAINS, which is the untried combination: chaining is what
keeps the path continuous, and only one constraint leaves the optimiser room to relax.
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
PATH = [3.20, 2.90, 2.65, 2.45, 2.35, 2.25, 2.15, 2.05, 1.95, 1.88]


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
    for d_form in PATH:
        v = cur[i_nu] - cur[i_c]; v /= np.linalg.norm(v)
        cur = cur.copy()
        cur[nu_from:] += (d_form - np.linalg.norm(cur[i_nu] - cur[i_c])) * v
        d_break = float(np.linalg.norm(cur[i_lg] - cur[i_c]))   # free to relax
        m = mol(S, cur, chrg)
        psi4.set_options({
            'pcm': False,
            'optking__frozen_distance': '%d %d' % (i_c + 1, i_nu + 1),
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
    relaxed = [r[3] for r in res]
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
    # Rule 31: an unrelaxed maximum is an upper bound at a non-stationary geometry,
    # invisible to both the nan check and the smoothness check.
    if not relaxed[i]:
        print('    WARNING: maximum-energy point %d is UNRELAXED - no barrier reported' % i)
        return dict(barrier=float('nan'), unrelaxed_max=True, rel=rel.tolist())
    n_un = sum(1 for x in relaxed if not x)
    print('    profile smooth (max step %.1f kcal/mol), %d/%d points unrelaxed'
          % (jumps.max(), n_un, len(relaxed)))
    return dict(barrier=float(rel[i]), i_ts=i, max_step=float(jumps.max()),
                rel=rel.tolist(), failed=0, n_unrelaxed=n_un)


def main():
    out = {}
    print('=== KINETIC CONTROL v2: two-bond coordinate ===')
    print('    expectation: SELENOLATE HAS THE LOWER BARRIER\n', flush=True)
    for nu in ['Se', 'S']:
        S, P = sn2_geom(nu)
        r = scan('ctl-' + nu, S, P, -1)
        out['ctl_' + nu] = summarise('ctl-' + nu, r)
        out['ctl_' + nu]['path'] = [(a, b) for a, b, _e, _ok in r]
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

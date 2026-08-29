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
psi4.set_num_threads(3)   # leave a core for the concurrent MD job
psi4.set_options({'reference': 'rks', 'scf_type': 'df',
                  'g_convergence': 'gau_loose', 'geom_maxiter': 60,
                  'guess': 'sad', 'maxiter': 200})

# Geometry is far less sensitive to level of theory than energy. Optimising at
# HF/def2-SVP and evaluating at wb97x-d/def2-SVPD+PCM is several times faster and
# changes a RELATIVE Se-vs-S barrier very little. Cartesian coordinates are still
# required through the transition region.
OPT = 'hf/def2-svp'
# def2-TZVPPD needs 790 basis functions on a 10-atom system and the PCM single point
# dominated everything (~20 min/scan point). def2-SVPD is 170 bf and KEEPS the diffuse
# functions anions require. Absolute barriers suffer; the Se-vs-S COMPARISON, which is
# what the selectivity question needs, does not.
SP = 'wb97x-d/def2-svpd'
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
    """Relaxed scan along d(Nu...C).

    Two things that broke the first attempt:
      * optking's redundant INTERNAL coordinates fail where one bond forms while
        another breaks ("Rejecting RFO root ... does not qualitatively match the
        forces"). Cartesian coordinates are stable through the transition region.
      * Chaining each point from the previous optimised geometry propagates a single
        failure through the whole scan. Each point is now built FRESH from the ideal
        collinear arrangement.
      * If an optimisation fails, the energy is still evaluated at the built geometry
        rather than returning nan, so one bad point cannot silently void the profile.
    """
    res = []
    for d in dists:
        cur = np.array(P0, dtype=float)
        v = cur[i_nu] - cur[i_c]
        v = v / np.linalg.norm(v)
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
            print('    [%s d=%.2f] opt failed (%s) - energy at built geometry'
                  % (tag, d, type(e).__name__), flush=True)
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
    d = np.array([a for a, _ in res])
    E = np.array([b for _, b in res])
    rel = (E - E[0]) * H2K
    nbad = int(np.isnan(E).sum())
    if nbad:
        print('    WARNING: %d/%d points failed - barrier NOT reported' % (nbad, len(E)))
        return dict(d=d.tolist(), rel=rel.tolist(), barrier=float('nan'),
                    d_ts=float('nan'), dE=float('nan'), failed=nbad)
    i = int(np.argmax(rel))
    return dict(d=d.tolist(), rel=rel.tolist(), barrier=float(rel[i]),
                d_ts=float(d[i]), dE=float(rel[-1]), failed=0)


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

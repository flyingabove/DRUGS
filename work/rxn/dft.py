# -*- coding: utf-8 -*-
"""TIER 1 at DFT — the selectivity calculation xtb could not do.

Rule 12/20: the SN2 control runs FIRST. Selenolate is experimentally the better
nucleophile; if the method says otherwise, nothing downstream is trusted.
Rule 23: this script prints tables only. Interpretation goes in the document.

Basis-set note: every nucleophile here is an ANION. Anions require DIFFUSE
functions - plain def2-SVP/def2-TZVP would badly overestimate their energies and
could invert the very comparison being made. Hence def2-SVPD / def2-TZVPPD.
"""
import sys, json, traceback
import psi4
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem
RDLogger.DisableLog('rdApp.*')

H2K = 627.5094740631
psi4.set_memory('3500 MB')
psi4.core.set_output_file('psi4.log', False)
psi4.set_num_threads(4)

OPT_LEVEL = 'wb97x-d/def2-svpd'      # diffuse-augmented: required for anions
SP_LEVEL  = 'wb97x-d/def2-tzvppd'

psi4.set_options({'reference': 'rks', 'scf_type': 'df',
                  'g_convergence': 'gau', 'geom_maxiter': 150,
                  'guess': 'sad', 'maxiter': 200})

HAVE_PCM = None   # determined at runtime

# psi4 requires each block's braces on their own lines - inline braces are a parse error
PCM_INPUT = '''
units = angstrom
medium {
  solvertype = iefpcm
  solvent = water
}
cavity {
  radiiset = bondi
  type = gepol
  area = 0.3
}
'''


def geom_from_smiles(smi, seed=17, nconf=8):
    m = Chem.AddHs(Chem.MolFromSmiles(smi))
    cids = list(AllChem.EmbedMultipleConfs(m, numConfs=nconf, randomSeed=seed))
    try:
        AllChem.MMFFOptimizeMoleculeConfs(m, maxIters=800)
    except Exception:
        pass
    best, be = cids[0], 1e9
    for c in cids:
        try:
            mp = AllChem.MMFFGetMoleculeProperties(m)
            ff = AllChem.MMFFGetMoleculeForceField(m, mp, confId=c)
            e = ff.CalcEnergy()
        except Exception:
            e = 0.0
        if e < be:
            be, best = e, c
    P = m.GetConformer(best).GetPositions()
    S = [a.GetSymbol() for a in m.GetAtoms()]
    return S, P


def psi4_mol(S, P, chrg, mult=1):
    lines = ["%d %d" % (chrg, mult)]
    for s, p in zip(S, P):
        lines.append("%s %.8f %.8f %.8f" % (s, p[0], p[1], p[2]))
    lines += ["units angstrom", "no_reorient", "no_com"]
    return psi4.geometry("\n".join(lines))


def try_enable_pcm():
    """PCMSolver is not in every psi4 build. Detect rather than assume."""
    global HAVE_PCM
    if HAVE_PCM is not None:
        return HAVE_PCM
    try:
        psi4.set_options({'pcm': True, 'pcm_scf_type': 'total'})
        psi4.pcm_helper(PCM_INPUT)
        m = psi4_mol(['O', 'H', 'H'],
                     [[0, 0, 0], [0.96, 0, 0], [-0.24, 0.93, 0]], 0)
        psi4.energy('hf/sto-3g', molecule=m)
        psi4.core.clean()
        HAVE_PCM = True
    except Exception:
        psi4.set_options({'pcm': False})
        HAVE_PCM = False
    return HAVE_PCM


def opt_then_sp(smi, chrg, tag):
    """Optimise in GAS PHASE (analytic gradients), single-point with PCM.

    psi4 has no analytic PCM gradients - it silently falls back to finite
    differences, which costs ~6N SCF evaluations per geometry step and made the
    first attempt intractable on a 5-atom molecule. Gas-phase geometry + implicit
    solvent single-point is the standard and robust protocol.
    """
    S, P = geom_from_smiles(smi)
    mol = psi4_mol(S, P, chrg)
    psi4.set_options({'pcm': False})          # gas-phase geometry
    try:
        psi4.optimize(OPT_LEVEL, molecule=mol)
    except Exception as e:
        print("    [%s] opt did not converge (%s) - using last geometry"
              % (tag, type(e).__name__))
    if HAVE_PCM:                              # solvated single-point
        psi4.set_options({'pcm': True, 'pcm_scf_type': 'total'})
        psi4.pcm_helper(PCM_INPUT)
    E = psi4.energy(SP_LEVEL, molecule=mol)
    psi4.set_options({'pcm': False})
    psi4.core.clean()
    return float(E)


CONTROL = [('MeSe_anion', '[CH3][Se-]', -1),
           ('MeS_anion',  '[CH3][S-]',  -1),
           ('MeBr',       'CBr',         0),
           ('Br_anion',   '[Br-]',      -1),
           ('MeSeMe',     'C[Se]C',      0),
           ('MeSMe',      'CSC',         0)]

TARGET = [('elec',   'CN(C)C(=O)C#[N+][O-]',          0),
          ('add_Se', 'CN(C)C(=O)C(=[N+][O-])[Se]C',  -1),
          ('add_S',  'CN(C)C(=O)C(=[N+][O-])SC',     -1)]


def main():
    pcm = try_enable_pcm()
    print("Level: opt %s | SP %s" % (OPT_LEVEL, SP_LEVEL))
    print("Solvent: %s\n" % ("IEFPCM water" if pcm else "GAS PHASE (PCMSolver unavailable)"))

    E = {}
    print("--- species ---")
    for tag, smi, q in (CONTROL + TARGET if '--all' in sys.argv else CONTROL):
        try:
            E[tag] = opt_then_sp(smi, q, tag)
            print("  %-12s %-32s chg%+d  E = %.8f" % (tag, smi, q, E[tag]))
        except Exception:
            print("  %-12s FAILED" % tag)
            traceback.print_exc()
            return

    print("\n--- CONTROL: CH3Br + Nu(-) -> CH3Nu + Br(-) ---")
    dSe = (E['MeSeMe'] + E['Br_anion'] - E['MeBr'] - E['MeSe_anion']) * H2K
    dS = (E['MeSMe'] + E['Br_anion'] - E['MeBr'] - E['MeS_anion']) * H2K
    print("  dE(Se)  = %+8.2f kcal/mol" % dSe)
    print("  dE(S)   = %+8.2f kcal/mol" % dS)
    print("  Se - S  = %+8.2f kcal/mol" % (dSe - dS))

    print("\n--- TARGET: nitrile oxide + Nu(-) -> adduct ---")
    rSe = (E['add_Se'] - E['elec'] - E['MeSe_anion']) * H2K
    rS = (E['add_S'] - E['elec'] - E['MeS_anion']) * H2K
    print("  dE(Se)  = %+8.2f kcal/mol" % rSe)
    print("  dE(S)   = %+8.2f kcal/mol" % rS)
    print("  Se - S  = %+8.2f kcal/mol" % (rSe - rS))

    json.dump({'level': [OPT_LEVEL, SP_LEVEL], 'pcm': pcm, 'E': E,
               'ctl_Se': dSe, 'ctl_S': dS, 'ctl_diff': dSe - dS,
               'rx_Se': rSe, 'rx_S': rS, 'rx_diff': rSe - rS},
              open('dft_results.json', 'w'), indent=1)
    print("\n-> dft_results.json")


if __name__ == '__main__':
    main()

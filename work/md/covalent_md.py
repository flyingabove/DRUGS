# -*- coding: utf-8 -*-
"""TIER 2 — explicit-solvent MD of the tethered GPX4-M3 adduct.

Question (2.4): do the N-methylamide arms — the ONLY change from ML210 — stay
solvent-facing once the protein is allowed to move? Every result so far came from a
RIGID receptor, which is the standing caveat on the 0.29 A anchored fit.

Simplifications, stated rather than hidden:
  * Sec46 -> CYS. Selenium has no standard force-field parameters. For a
    SOLVENT-EXPOSURE question at atoms 10+ A from the reacting centre this is
    immaterial; it would NOT be acceptable for energetics, and we compute none.
  * The covalent bond is a stiff harmonic restraint (Cys46 SG ... ligand C),
    not a bonded term, which avoids retypeing the residue.
  * The ligand's attachment carbon is H-capped for parameterisation. That H is a
    known artifact sitting where the Se-C bond would be.
"""
import sys, json
import numpy as np
import openmm as mm
import openmm.app as app
import openmm.unit as u
from openff.toolkit import Molecule
from openmmforcefields.generators import SMIRNOFFTemplateGenerator
from pdbfixer import PDBFixer

RECEPTOR = '../structures/6HKQ_receptor_CYSsurrogate.pdb'
# M3 adduct in its BONDED form: SeCH3 removed, attachment carbon H-capped
LIG = 'CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)C=NO)CC2)cc1'
NS = float(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else 20.0
DRY = '--dry' in sys.argv


def find_cys46_sg(pdb):
    for res in pdb.topology.residues():
        if res.name in ('CYS', 'SEC', 'CSE') and res.id.strip() == '46':
            for a in res.atoms():
                if a.name in ('SG', 'SE'):
                    return a.index
    raise SystemExit('Cys/Sec 46 SG not found — check the receptor file')


def main():
    # The deposited receptor has no hydrogens and may have missing side-chain atoms.
    # PDBFixer must run BEFORE the SG index is taken - adding hydrogens renumbers
    # every atom, so an index captured from the raw file would point somewhere else.
    fixer = PDBFixer(filename=RECEPTOR)
    fixer.findMissingResidues()
    fixer.missingResidues = {}          # do not build unresolved loops
    fixer.findMissingAtoms()
    fixer.addMissingAtoms()
    fixer.addMissingHydrogens(7.4)
    pdb = fixer
    sg = find_cys46_sg(fixer)
    print('receptor atoms %d (H added) | Cys46 SG index %d'
          % (fixer.topology.getNumAtoms(), sg))

    # Load from the SDF written by make_pose.py: it carries BOTH the topology and the
    # anchored coordinates in one consistent atom ordering. Rebuilding from SMILES here
    # would give a different ordering than m3_pose.npy and silently scramble the pose.
    off = Molecule.from_file('m3_lig.sdf', allow_undefined_stereo=True)
    if isinstance(off, list):
        off = off[0]
    print('ligand atoms %d  net charge %s' % (off.n_atoms, off.total_charge))

    smirnoff = SMIRNOFFTemplateGenerator(molecules=off, forcefield='openff-2.2.0')
    ff = app.ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')
    ff.registerTemplateGenerator(smirnoff.generator)

    # Start from the ANCHORED POSE computed by the fit, not an arbitrary offset:
    # dropping the ligand near the protein at random would start the run inside a
    # steric clash that minimisation may not resolve cleanly.
    lig_top = off.to_topology().to_openmm()
    import os
    if not os.path.exists('m3_pose.npy'):
        raise SystemExit('m3_pose.npy missing - run make_pose.py first')
    lig_xyz = np.load('m3_pose.npy') / 10.0          # Angstrom -> nm
    assert lig_xyz.shape[0] == off.n_atoms, (
        'pose has %d atoms, ligand has %d' % (lig_xyz.shape[0], off.n_atoms))
    print('using anchored pose from m3_pose.npy')

    modeller = app.Modeller(pdb.topology, pdb.positions)
    modeller.add(lig_top, lig_xyz * u.nanometer)
    lig_start = pdb.topology.getNumAtoms()
    print('complex atoms %d' % modeller.topology.getNumAtoms())

    modeller.addSolvent(ff, padding=1.0 * u.nanometer, ionicStrength=0.15 * u.molar,
                        model='tip3p')
    print('solvated atoms %d' % modeller.topology.getNumAtoms())
    if DRY:
        print('DRY RUN — setup validated, no dynamics run')
        return

    system = ff.createSystem(modeller.topology, nonbondedMethod=app.PME,
                             nonbondedCutoff=1.0 * u.nanometer,
                             constraints=app.HBonds, rigidWater=True)
    # tether: ligand attachment carbon (the sp2 C bearing =N-O-) to Cys46 SG
    # attachment carbon = the ligand atom closest to Cys46 SG in the anchored pose,
    # which is exactly where the Se-C bond was. Identify it geometrically, then ASSERT
    # it is the sp2 oxime carbon rather than trusting a SMARTS pattern (Rule 21).
    sgpos_A = np.array(pdb.positions.value_in_unit(u.angstrom))[sg]
    pose_A = np.load('m3_pose.npy')
    heavy = [i for i, a in enumerate(off.atoms) if a.symbol != 'H']
    di = min(heavy, key=lambda i: np.linalg.norm(pose_A[i] - sgpos_A))
    at = off.atoms[di]
    nb = [n.symbol for b in at.bonds for n in (b.atom1, b.atom2) if n is not at]
    print('attachment candidate: %s, neighbours %s, %.2f A from SG'
          % (at.symbol, nb, np.linalg.norm(pose_A[di] - sgpos_A)))
    assert at.symbol == 'C' and 'N' in nb, 'attachment atom is not the oxime carbon'
    attach = lig_start + di
    print('tethering ligand atom %d to SG %d' % (attach, sg))
    bond = mm.HarmonicBondForce()
    bond.addBond(sg, attach, 0.182 * u.nanometer,
                 200000.0 * u.kilojoule_per_mole / u.nanometer ** 2)
    system.addForce(bond)

    integrator = mm.LangevinMiddleIntegrator(310 * u.kelvin, 1.0 / u.picosecond,
                                             2.0 * u.femtosecond)
    system.addForce(mm.MonteCarloBarostat(1 * u.bar, 310 * u.kelvin))
    plat = mm.Platform.getPlatformByName('OpenCL')
    sim = app.Simulation(modeller.topology, system, integrator, plat)
    sim.context.setPositions(modeller.positions)
    print('minimising...')
    sim.minimizeEnergy(maxIterations=5000)
    sim.context.setVelocitiesToTemperature(310 * u.kelvin)
    print('equilibrating 200 ps...')
    sim.step(100000)
    app.PDBFile.writeFile(sim.topology,
                          sim.context.getState(getPositions=True).getPositions(),
                          open('equil.pdb', 'w'))
    sim.reporters.append(app.DCDReporter('traj.dcd', 10000))
    sim.reporters.append(app.StateDataReporter(sys.stdout, 50000, step=True,
                                               potentialEnergy=True, temperature=True,
                                               speed=True, remainingTime=True,
                                               totalSteps=int(NS * 5e5)))
    print('producing %.1f ns' % NS)
    sim.step(int(NS * 5e5))
    json.dump({'lig_start': lig_start, 'attach': attach, 'sg': sg,
               'n_lig': off.n_atoms}, open('md_meta.json', 'w'), indent=1)
    print('done -> traj.dcd')


if __name__ == '__main__':
    main()

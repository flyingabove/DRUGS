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
    pdb = app.PDBFile(RECEPTOR)
    sg = find_cys46_sg(pdb)
    print('receptor atoms %d | Cys46 SG index %d' % (pdb.topology.getNumAtoms(), sg))

    off = Molecule.from_smiles(LIG, allow_undefined_stereo=True)
    off.generate_conformers(n_conformers=1)
    print('ligand atoms %d  net charge %s' % (off.n_atoms, off.total_charge))

    smirnoff = SMIRNOFFTemplateGenerator(molecules=off, forcefield='openff-2.2.0')
    ff = app.ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')
    ff.registerTemplateGenerator(smirnoff.generator)

    # Start from the ANCHORED POSE computed by the fit, not an arbitrary offset:
    # dropping the ligand near the protein at random would start the run inside a
    # steric clash that minimisation may not resolve cleanly.
    lig_top = off.to_topology().to_openmm()
    import os
    if os.path.exists('m3_pose.npy'):
        lig_xyz = np.load('m3_pose.npy') / 10.0      # Angstrom -> nm
        print('using anchored pose from m3_pose.npy')
        assert lig_xyz.shape[0] == off.n_atoms, (
            'pose has %d atoms, ligand has %d' % (lig_xyz.shape[0], off.n_atoms))
    else:
        raise SystemExit('m3_pose.npy missing - run qmcluster/burial_m3.py first')

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
    attach = None
    for a in off.atoms:
        if a.symbol == 'C' and any(b.bond_order == 2 and
                                   (b.atom1.symbol == 'N' or b.atom2.symbol == 'N')
                                   for b in a.bonds):
            nbrs = [n.symbol for b in a.bonds for n in (b.atom1, b.atom2) if n is not a]
            if 'H' in nbrs and 'C' in nbrs:
                attach = lig_start + a.molecule_atom_index
                break
    if attach is None:
        attach = lig_start
        print('WARNING: attachment atom not identified by pattern; using first ligand atom')
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

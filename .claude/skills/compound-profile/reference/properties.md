# Molecular Property Reference

Reference for calculating and interpreting molecular properties relevant to drug discovery.

## Key Properties

### Physicochemical Properties

| Property | Symbol | Typical Range | Description |
|----------|--------|---------------|-------------|
| Molecular Weight | MW | 150-500 Da | Mass of molecule |
| LogP | AlogP/LogP | -2 to 5 | Lipophilicity (octanol/water) |
| LogD | LogD | pH-dependent | Distribution coefficient |
| pKa | pKa | varies | Acid/base dissociation constant |
| PSA | TPSA | <140 Ų | Topological polar surface area |
| Rotatable Bonds | RTB | ≤10 | Rotatable bond count |
| H-Bond Donors | HBD | ≤5 | Hydrogen bond donors |
| H-Bond Acceptors | HBA | ≤10 | Hydrogen bond acceptors |
| Aromatic Rings | - | ≤3 | Number of aromatic rings |
| Heavy Atoms | - | varies | Non-hydrogen atoms |
| Fsp3 | Fsp3 | ≥0.4 | Fraction sp3 carbons |

## Drug-Likeness Rules

### Lipinski's Rule of 5 (Ro5)

A compound is likely orally active if it violates ≤1 rule:

| Rule | Threshold |
|------|-----------|
| Molecular weight | ≤500 Da |
| LogP | ≤5 |
| H-bond donors | ≤5 |
| H-bond acceptors | ≤10 |

**Note**: Multiples of 5 give the rule its name.

### Veber Rules

For good oral bioavailability:

| Rule | Threshold |
|------|-----------|
| Rotatable bonds | ≤10 |
| Polar surface area | ≤140 Ų (or ≤12 H-bond donors/acceptors) |

### Pfizer's 3/75 Rule

For reduced attrition:

| Rule | Threshold |
|------|-----------|
| LogP | <3 |
| pKa (basic) | <8 |

### Ghose Filters

| Rule | Threshold |
|------|-----------|
| Molecular weight | 160-480 Da |
| LogP | -0.4 to 5.6 |
| Atom count | 20-70 |
| Aromatic rings | 0-7 |
| Fsp3 | >0.15 |

### Egan Rules

| Rule | Threshold |
|------|-----------|
| LogP | ≤5.88 |
| PSA | ≤131.6 Ų |

### MDDR-like Rule

| Rule | Threshold |
|------|-----------|
| Molecular weight | 200-600 Da |
| LogP | -2 to 5 |
| Ring count | ≤6 |
| H-bond donors | ≤5 |
| H-bond acceptors | ≤10 |
| Rotatable bonds | ≤15 |

## Lead-Likeness

### Congreve Rules

For lead-like compounds (more optimization potential):

| Rule | Threshold |
|------|-----------|
| Molecular weight | ≤350 Da |
| LogP | ≤3 |
| Rotatable bonds | ≤7 |

### Oprea Criteria

| Rule | Threshold |
|------|-----------|
| Molecular weight | 350-500 Da |
| LogP | -2 to 5 |
| Ring count | 3-7 |
| Rotatable bonds | ≤8 |
| H-bond donors | ≤5 |
| H-bond acceptors | ≤10 |

## PAINS Filters

Pan-Assay Interference Compounds (PAINS) are frequent assay hitters.

### Common PAINS Substructures

| Substructure | Name | Description |
|--------------|------|-------------|
| Rhodanines | Thiocarbonyl | Metal chelation |
| Curcuminoids | Enone | Redox activity |
| Quinones | Quinone | Redox cycling |
| Catechols | Catechol | Metal binding |
| Enones | Michael acceptor | Covalent modification |

### Filtering

Use RDKit or PAINS filters to flag problematic substructures.

## Property Calculations

### From SMILES (RDKit)

```python
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski

def calculate_properties(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return None

    return {
        "mw": Descriptors.MolWt(mol),
        "logp": Descriptors.MolLogP(mol),
        "hbd": Lipinski.NumHDonors(mol),
        "hba": Lipinski.NumHAcceptors(mol),
        "tpsa": Descriptors.TPSA(mol),
        "rotb": Lipinski.NumRotatableBonds(mol),
        "aromatic_rings": Lipinski.NumAromaticRings(mol),
        "heavy_atoms": Lipinski.HeavyAtomCount(mol),
        "fsp3": Descriptors.FractionCsp3(mol),
        "ro5_violations": sum([
            Descriptors.MolWt(mol) > 500,
            Descriptors.MolLogP(mol) > 5,
            Lipinski.NumHDonors(mol) > 5,
            Lipinski.NumHAcceptors(mol) > 10
        ])
    }
```

### From InChI

```python
mol = Chem.MolFromInchi(inchi_string)
properties = calculate_properties_from_mol(mol)
```

## Property Interpretation

### LogP Interpretation

| Range | Interpretation |
|-------|----------------|
| <0 | Very hydrophilic |
| 0-1 | Hydrophilic |
| 1-2 | Moderately hydrophilic |
| 2-3 | Balanced |
| 3-4 | Moderately lipophilic |
| 4-5 | Lipophilic |
| >5 | Very lipophilic |

### PSA Interpretation

| Range | Interpretation |
|-------|----------------|
| <75 Ų | Good oral/cell penetration |
| 75-140 Ų | Moderate penetration |
| >140 Ų | Poor oral/cell penetration |
| >180 Ų | Likely CNS-impermeable |

### Solubility Prediction (ESOL)

```python
# Simplified ESOL model
logS = 0.16 - 0.63*logP - 0.0062*MW + 0.066*RB - 0.74*AP
```

Where:
- RB = rotatable bonds
- AP = aromatic proportion

### Blood-Brain Barrier Permeability

**Rule of thumb**: BBB permeable if:
- PSA < 90 Ų
- LogP 2-4
- MW < 450 Da

## Property Distributions by Drug Class

### Oral Small Molecules

| Property | Median | Range |
|----------|--------|-------|
| MW | 350 | 250-500 |
| LogP | 2.5 | -1 to 6 |
| HBD | 2 | 0-5 |
| HBA | 4 | 1-10 |
| PSA | 75 | 20-140 |
| RTB | 5 | 0-10 |

### CNS Drugs

| Property | Median | Range |
|----------|--------|-------|
| MW | 300 | 200-450 |
| LogP | 2.8 | 1-5 |
| HBD | 1 | 0-3 |
| HBA | 3 | 1-7 |
| PSA | 50 | 20-90 |
| RTB | 4 | 0-8 |

### IV Drugs

| Property | Median | Range |
|----------|--------|-------|
| MW | 500 | 300-1000 |
| LogP | 1 | -3 to 5 |
| HBD | 3 | 0-8 |
| HBA | 6 | 2-15 |
| PSA | 140 | 50-250 |
| RTB | 8 | 0-15 |

## Property Optimization Strategies

### Reduce LogP

- Add polar groups (alcohols, amines)
- Remove hydrophobic groups
- Introduce heteroatoms
- Ring opening

### Reduce PSA

- Mask polar groups (esters, amides)
- Reduce ionizable groups
- Replace with bioisosteres

### Reduce MW

- Remove unnecessary substituents
- Replace phenyl with heterocycle
- Scaffold hopping

### Improve Solubility

- Reduce LogP
- Increase PSA
- Add ionizable groups
- Reduce crystal packing (add asymmetry)

## Resources

### Tools

- **RDKit**: Open-source cheminformatics
- **ChemAxon**: Commercial calculators
- **Molinspiration**: Web-based property calculator
- **SwissADME**: Free ADME prediction

### Databases

- **ChEMBL**: Bioactive molecules with properties
- **PubChem**: Compound database
- **DrugBank**: Approved drug properties

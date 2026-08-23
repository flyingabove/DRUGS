# Background: Machine Learning for Drug Discovery

## Overview

This project explores how machine learning (ML) can be applied to drug
discovery — the process of identifying and designing new chemical compounds
that can become safe, effective medicines. Traditional drug discovery is
slow and expensive (often 10+ years and $1B+ per approved drug), largely
because the space of possible drug-like molecules is astronomically large
(estimated at 10^23–10^60 candidates) and most fail late in the pipeline due
to poor efficacy, toxicity, or pharmacokinetics. ML aims to make this search
faster and cheaper by predicting molecular properties and generating
promising candidates computationally before costly lab synthesis and
testing.

## Where ML Fits in the Drug Discovery Pipeline

1. **Target identification** — finding the biological molecule (usually a
   protein) associated with a disease.
2. **Hit discovery / virtual screening** — searching large compound
   libraries for molecules likely to bind a target.
3. **Lead optimization** — refining a promising "hit" molecule to improve
   potency, selectivity, and drug-like properties.
4. **ADMET prediction** — estimating Absorption, Distribution, Metabolism,
   Excretion, and Toxicity before synthesis.
5. **Preclinical / clinical trials** — ML is increasingly used to predict
   trial outcomes and identify patient subgroups, though this project
   focuses primarily on stages 1–4.

## Core ML Approaches

### Molecular representation
Molecules must be converted into a form ML models can use:
- **SMILES strings** — a text encoding of molecular structure, usable with
  NLP-style sequence models (RNNs, Transformers).
- **Molecular graphs** — atoms as nodes, bonds as edges; used with Graph
  Neural Networks (GNNs) such as Message Passing Neural Networks (MPNN),
  GCN, and GAT.
- **3D structures** — atom coordinates in space, used for models that need
  spatial/geometric awareness (e.g., protein-ligand binding).
- **Fingerprints/descriptors** — fixed-length vectors (e.g., Morgan/ECFP
  fingerprints) for classical ML (random forests, gradient boosting).

### Property prediction
Supervised models trained on labeled data to predict:
- Binding affinity to a target protein
- Toxicity, solubility, permeability (ADMET properties)
- Synthesizability (how feasible a molecule is to make)

### Generative models (de novo molecule design)
Models that propose novel molecular structures rather than just scoring
existing ones:
- **Variational Autoencoders (VAEs)** — learn a continuous latent space of
  molecules that can be sampled and decoded into new structures.
- **Generative Adversarial Networks (GANs)** — generator/discriminator pairs
  trained to produce realistic molecules.
- **Diffusion models** — increasingly used for 3D molecule and conformer
  generation.
- **Reinforcement Learning (RL)** — an agent iteratively edits or builds
  molecules to optimize a reward function (e.g., predicted binding affinity
  combined with drug-likeness).
- **Autoregressive Transformers** — generate SMILES or graphs token-by-token,
  similar to language modeling.

### Structure-based methods
- **Protein structure prediction** (e.g., AlphaFold, ESMFold) provides 3D
  target structures when experimental structures are unavailable.
- **Docking simulations** estimate how well a candidate molecule binds a
  target's binding site; ML models are increasingly used to speed up or
  replace traditional physics-based docking.
- **Protein-ligand interaction models** predict binding affinity directly
  from 3D structures (e.g., using GNNs or equivariant neural networks).

## Common Datasets and Benchmarks
- **ZINC** — large library of purchasable, drug-like compounds for
  virtual screening.
- **ChEMBL** — bioactivity data curated from scientific literature.
- **PubChem** — large public repository of chemical structures and assay
  results.
- **PDBBind** — protein-ligand complexes with experimental binding
  affinities, used for structure-based models.
- **MoleculeNet** — a benchmark suite covering property prediction tasks
  across multiple datasets.
- **Tox21 / ToxCast** — toxicity screening datasets.

## Key Tools and Libraries
- **RDKit** — cheminformatics toolkit for molecule parsing, descriptors,
  and fingerprints.
- **DeepChem** — ML library built for chemistry and drug discovery tasks.
- **PyTorch Geometric / DGL** — graph neural network frameworks commonly
  used for molecular graphs.
- **OpenMM / AutoDock Vina** — molecular simulation and docking tools,
  sometimes combined with ML surrogates.

## Challenges
- **Data scarcity and bias** — labeled bioactivity data is limited and
  skewed toward well-studied targets.
- **Generalization** — models often perform poorly on novel chemical
  scaffolds outside their training distribution.
- **Synthesizability gap** — generative models can propose molecules that
  are difficult or impossible to actually synthesize.
- **Validation cost** — computational predictions still require expensive
  wet-lab validation to confirm real-world efficacy and safety.
- **Interpretability** — understanding *why* a model favors a candidate
  matters for trust and regulatory acceptance.

## Notes
This document is a starting reference for the project and will be expanded
as specific research directions (e.g., a target disease, a particular model
architecture, or a benchmark to focus on) are chosen.

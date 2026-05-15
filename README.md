# Open Quantum System Dynamics with OQuPy

This repository contains a compact portfolio project on open quantum system dynamics using **OQuPy**.

The project focuses on the dynamics of a two-level quantum system coupled to a bosonic environment, illustrating key physical concepts such as decoherence, relaxation, memory effects, and non-Markovian dynamics.

## Overview

Open quantum systems are quantum systems that interact with an external environment. Instead of evolving purely unitarily, their dynamics can include dissipation, decoherence, relaxation, and memory effects.

OQuPy is a Python package designed to simulate non-Markovian open quantum systems using process tensors and tensor-network-based methods.

## Physical Model

The main example considered in this repository is a two-level system described by a Hamiltonian of the form

```math
H_S =
\frac{\epsilon}{2}\sigma_z
+
\frac{\Delta}{2}\sigma_x,
```

where:

- $\epsilon$ is the energy bias;
- $\Delta$ is the tunneling amplitude;
- $\sigma_x$ and $\sigma_z$ are Pauli matrices.

The system is coupled to a bosonic environment through an operator such as

```math
A = \sigma_z.
```

This type of model is closely related to the spin-boson model, which is widely used to study decoherence and relaxation in quantum systems.

## Goals

This repository aims to demonstrate:

- construction of a simple open quantum system model;
- simulation of time-dependent reduced dynamics;
- computation of expectation values such as $\langle \sigma_z(t) \rangle$ and $\langle \sigma_x(t) \rangle$;
- visualization of decoherence and relaxation;
- reproducible scientific Python workflows using OQuPy.

## Repository Structure

```text
open-quantum-system-dynamics-oqupy/
├── README.md
├── requirements.txt
├── src/
│   ├── run_oqupy_dynamics.py
│   └── plot_results.py
├── results/
│   └── .gitkeep
└── figures/
    └── .gitkeep
```

## Planned Workflow

1. Define the two-level quantum system.
2. Define the system-environment coupling.
3. Specify bath correlations.
4. Run the OQuPy dynamics simulation.
5. Save expectation values.
6. Generate plots of open-system dynamics.

## Requirements

```text
numpy
matplotlib
oqupy
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Expected Outputs

The project will generate:

- numerical data in `results/`;
- plots of time-dependent expectation values in `figures/`;
- examples of decoherence and relaxation dynamics.

## Status

This repository is under active development.

The first version focuses on a minimal two-level-system example using OQuPy.

## Author

Thiago Rocha Girão Souza  
PhD Candidate in Physics  
Quantum Computing | Quantum Dynamics | Scientific Python

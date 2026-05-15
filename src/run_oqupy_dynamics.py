"""
Open quantum system dynamics using OQuPy.

This script simulates a two-level system coupled to an Ohmic bosonic bath
using the TEMPO method implemented in OQuPy.
"""

from pathlib import Path

import numpy as np
import oqupy


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    results_dir = root / "results"
    results_dir.mkdir(exist_ok=True)

    # Pauli operators and initial state
    sigma_x = oqupy.operators.sigma("x")
    sigma_z = oqupy.operators.sigma("z")
    initial_state = oqupy.operators.spin_dm("z+")

    # Physical parameters
    omega = 1.0
    omega_cutoff = 5.0
    alpha = 0.3

    # Two-level system Hamiltonian: H_S = (omega / 2) sigma_x
    system = oqupy.System(0.5 * omega * sigma_x)

    # Ohmic spectral density with exponential cutoff
    correlations = oqupy.PowerLawSD(
        alpha=alpha,
        zeta=1,
        cutoff=omega_cutoff,
        cutoff_type="exponential",
    )

    # System-bath coupling through sigma_z / 2
    bath = oqupy.Bath(0.5 * sigma_z, correlations)

    # TEMPO numerical parameters
    tempo_parameters = oqupy.TempoParameters(
        dt=0.1,
        tcut=3.0,
        epsrel=1.0e-4,
    )

    # OQuPy's TEMPO computation
    dynamics = oqupy.tempo_compute(
        system=system,
        bath=bath,
        initial_state=initial_state,
        start_time=0.0,
        end_time=15.0,
        parameters=tempo_parameters,
        unique=False,
    )

    times, sigma_z_values = dynamics.expectations(0.5 * sigma_z, real=True)
    _, sigma_x_values = dynamics.expectations(0.5 * sigma_x, real=True)

    output_path = results_dir / "oqupy_open_system_dynamics.npz"

    np.savez(
        output_path,
        times=times,
        sigma_z=sigma_z_values,
        sigma_x=sigma_x_values,
        omega=omega,
        omega_cutoff=omega_cutoff,
        alpha=alpha,
        dt=tempo_parameters.dt,
        tcut=tempo_parameters.tcut,
        epsrel=tempo_parameters.epsrel,
    )

    print(f"Saved results to: {output_path}")
    print(f"Number of time points: {len(times)}")
    print(f"Bath coupling strength alpha: {alpha}")


if __name__ == "__main__":
    main()

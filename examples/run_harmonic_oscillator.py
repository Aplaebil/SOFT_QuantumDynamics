"""
Example script for a 1D harmonic oscillator.
"""

import numpy as np
import sys
sys.path.append("../src")

from initialize_system import initialize_system
from potential import potential_function
from evolve import evolve_wavefunction
from visualize import visualize_results

def main():
    # Parameters
    xmin, xmax = -10.0, 10.0
    N = 2**10
    x0 = 0.0
    sigma = 1.0
    k0 = 0.0
    hbar = 1.0
    m = 1.0
    omega = 1.0  # oscillator frequency
    dt = 0.01
    total_time = 5.0

    # Initialize system
    x, dx, psi, k, dk = initialize_system(xmin, xmax, N, x0, sigma, k0, hbar, m)

    # Harmonic potential
    V = potential_function(x, potential_type='harmonic', m=m, omega=omega)

    num_steps = int(total_time / dt)
    plot_interval = num_steps // 10

    for step in range(num_steps):
        psi = evolve_wavefunction(psi, V, dt, dx, k, hbar, m)

        if step % plot_interval == 0:
            visualize_results(x, psi, step, potential=V, save_fig=False)

    print("Harmonic oscillator simulation finished.")

if __name__ == "__main__":
    main()


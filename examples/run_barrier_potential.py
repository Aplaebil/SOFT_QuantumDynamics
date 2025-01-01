"""
Example script to demonstrate quantum tunneling through a barrier.
"""

import numpy as np
import sys
# Adjust import path if needed
sys.path.append("../src")

from initialize_system import initialize_system
from potential import potential_function
from evolve import evolve_wavefunction
from visualize import visualize_results

def main():
    # Simulation parameters
    xmin, xmax = -10.0, 10.0
    N = 2**10
    x0 = -5.0
    sigma = 1.0
    k0 = 3.0
    hbar = 1.0
    m = 1.0
    dt = 0.01
    total_time = 2.0

    # Initialize system
    x, dx, psi, k, dk = initialize_system(xmin, xmax, N, x0, sigma, k0, hbar, m)

    # Define barrier potential
    V0 = 10.0
    a = 1.0
    V = potential_function(x, potential_type='barrier', V0=V0, a=a)

    num_steps = int(total_time / dt)
    plot_interval = num_steps // 10

    for step in range(num_steps):
        psi = evolve_wavefunction(psi, V, dt, dx, k, hbar, m)

        if step % plot_interval == 0:
            visualize_results(x, psi, step, potential=V, save_fig=False)

    print("Barrier potential simulation finished.")

if __name__ == "__main__":
    main()


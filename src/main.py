"""
Entry point for running a default simulation using the SOFT method.
"""

import numpy as np
from initialize_system import initialize_system
from potential import potential_function
from evolve import evolve_wavefunction
from visualize import visualize_results

def main():
    # Example parameters for a quick run
    xmin, xmax = -10.0, 10.0
    N = 2**10
    x0 = -5.0
    sigma = 1.0
    k0 = 3.0
    hbar = 1.0
    m = 1.0
    dt = 0.01
    total_time = 2.0

    x, dx, psi, k, dk = initialize_system(xmin, xmax, N, x0, sigma, k0, hbar, m)

    # Potential: barrier
    V0 = 10.0
    a = 1.0
    V = potential_function(x, potential_type='barrier', V0=V0, a=a)

    num_steps = int(total_time / dt)
    for step in range(num_steps):
        psi = evolve_wavefunction(psi, V, dt, dx, k, hbar, m)

    visualize_results(x, psi, num_steps, potential=V, save_fig=False)
    print("Default simulation finished.")

if __name__ == "__main__":
    main()


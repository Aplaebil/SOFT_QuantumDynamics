"""
Example script demonstrating double-slit interference.
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
    x0 = -5.0
    sigma = 0.5
    k0 = 5.0
    hbar = 1.0
    m = 1.0
    dt = 0.005
    total_time = 2.0

    # Initialize system
    x, dx, psi, k, dk = initialize_system(xmin, xmax, N, x0, sigma, k0, hbar, m)

    # Double-slit potential
    V0 = 50.0  # barrier height
    V = potential_function(x, potential_type='double_slit', V0=V0)

    num_steps = int(total_time / dt)
    plot_interval = num_steps // 10

    for step in range(num_steps):
        psi = evolve_wavefunction(psi, V, dt, dx, k, hbar, m)

        if step % plot_interval == 0:
            visualize_results(x, psi, step, potential=V, save_fig=False)

    print("Double-slit simulation finished.")

if __name__ == "__main__":
    main()


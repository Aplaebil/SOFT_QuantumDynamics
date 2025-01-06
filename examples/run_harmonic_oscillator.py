"""
Example script for a 3D harmonic oscillator.
"""

import numpy as np
import sys

from src.initialize_system import initialize_system
from src.potential import potential_function
from src.evolve import evolve_wavefunction
from src.visualize import visualize_results_3d

def main():
    # --- Simulation Parameters ---
    xmin, xmax = -10.0, 10.0
    N = 64
    x0, y0, z0 = 0.0, 0.0, 0.0
    sigma = 1.0
    kx0, ky0, kz0 = 0.0, 0.0, 0.0  # no initial momentum

    hbar = 1.0
    m = 1.0
    omega = 1.0  # oscillator frequency (assume same in x,y,z)
    
    dt = 0.01
    total_time = 5.0

    # Initialize system (3D)
    (X, Y, Z,
     dx,
     psi,
     KX, KY, KZ,
     dk) = initialize_system(
         xmin, xmax, N,
         x0, y0, z0,
         sigma,
         kx0, ky0, kz0,
         hbar, m
    )

    # 3D Harmonic potential
    V = potential_function(X, Y, Z, potential_type='harmonic', m=m, omega=omega)

    num_steps = int(total_time / dt)
    plot_interval = max(1, num_steps // 10)

    for step in range(num_steps):
        psi = evolve_wavefunction(psi, V, dt, dx, KX, KY, KZ, hbar, m)

        if step % plot_interval == 0:
            visualize_results_3d(X, Y, psi, step, potential=V,
                                 z_index=N//2, save_fig=False)

    print("3D Harmonic oscillator simulation finished.")

if __name__ == "__main__":
    main()


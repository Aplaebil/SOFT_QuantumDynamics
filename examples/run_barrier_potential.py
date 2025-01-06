"""
Example script to demonstrate quantum tunneling through a 3D barrier (a "box" region).
"""

import numpy as np
import sys

from src.initialize_system import initialize_system
from src.potential import potential_function
from src.evolve import evolve_wavefunction
from src.visualize import visualize_results_3d

def main():
    # --- Simulation parameters ---
    xmin, xmax = -10.0, 10.0
    N = 64  # 3D grid: Nx=Ny=Nz=64 (adjust if too large for your memory)
    
    # Initial wave packet center & width
    x0, y0, z0 = -5.0, 0.0, 0.0
    sigma = 1.0
    
    # Initial wave numbers (momentum in x, y, z)
    kx0, ky0, kz0 = 3.0, 0.0, 0.0
    
    hbar = 1.0
    m = 1.0
    
    dt = 0.01
    total_time = 2.0

    # --- Initialize system (3D) ---
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

    # --- Define a 3D barrier potential ---
    # e.g., "box" barrier of width 2a around origin in y,z, but offset in x?
    # For simplicity, let's just place a cubic barrier around x=0,y=0,z=0
    V0 = 10.0
    a = 1.0
    V = potential_function(X, Y, Z, potential_type='barrier', V0=V0, a=a)

    # Steps & output intervals
    num_steps = int(total_time / dt)
    plot_interval = max(1, num_steps // 10)

    for step in range(num_steps):
        psi = evolve_wavefunction(psi, V, dt, dx, KX, KY, KZ, hbar, m)

        # Visualize every 10% of simulation
        if step % plot_interval == 0:
            visualize_results_3d(X, Y, psi, step, potential=V,
                                 z_index=N//2, save_fig=False)

    print("3D Barrier potential simulation finished.")

if __name__ == "__main__":
    main()


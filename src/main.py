"""
Entry point for running a default 3D simulation using the SOFT method.
"""

import numpy as np
from initialize_system import initialize_system
from potential import potential_function
from evolve import evolve_wavefunction
from visualize import visualize_results_3d  # <- a 3D visualization function

def main():
    # --- Example parameters for a quick 3D run ---
    xmin, xmax = -10.0, 10.0
    N = 64        # 3D grid size: Nx=Ny=Nz=N (64^3 might be large; adjust for speed)
    
    # Initial wave packet parameters
    x0, y0, z0 = -5.0, 0.0, 0.0
    sigma = 1.0
    kx0, ky0, kz0 = 3.0, 0.0, 0.0  # initial momentum mostly in +x direction

    hbar = 1.0
    m = 1.0
    dt = 0.01
    total_time = 2.0

    # --- Initialize the 3D system ---
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
    V0 = 10.0
    a = 1.0
    # 'barrier' in 3D might be a cubic region around x=0, y=0, z=0:
    V = potential_function(X, Y, Z, potential_type='barrier', V0=V0, a=a)

    # --- Main time evolution loop ---
    num_steps = int(total_time / dt)
    for step in range(num_steps):
        psi = evolve_wavefunction(psi, V, dt, dx, KX, KY, KZ, hbar, m)

    # --- Final visualization of a cross-section (z = mid-plane, for instance) ---
    visualize_results_3d(
        X, Y, psi,
        step=num_steps,
        potential=V,
        z_index=N//2,
        save_fig=False
    )
    print("3D default simulation finished.")

if __name__ == "__main__":
    main()


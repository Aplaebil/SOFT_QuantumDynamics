"""
Example script demonstrating double-slit-like interference in 3D.
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
    x0, y0, z0 = -8.0, 0.0, 0.0
    sigma = 0.5
    kx0, ky0, kz0 = 5.0, 0.0, 0.0  # heading in +x direction

    hbar = 1.0
    m = 1.0
    dt = 0.005
    total_time = 2.0

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

    # 3D "double-slit" potential: you can define "barriers" around x=0, but open slits in y,z
    # For demonstration, let's define it as a custom potential:
    V0 = 50.0
    V = double_slit_3d(X, Y, Z, V0)  # We'll define a local function below

    num_steps = int(total_time / dt)
    plot_interval = max(1, num_steps // 10)

    for step in range(num_steps):
        psi = evolve_wavefunction(psi, V, dt, dx, KX, KY, KZ, hbar, m)

        if step % plot_interval == 0:
            visualize_results_3d(X, Y, psi, step, potential=V,
                                 z_index=N//2, save_fig=False)

    print("3D Double-slit simulation finished.")

def double_slit_3d(X, Y, Z, V0):
    """
    Return a 3D potential array that models two slits in the yz-plane at x=0.
    Slits are open in two bands of y, otherwise there's a barrier of height V0.
    """
    V = np.zeros_like(X)
    # We'll define a region around x=0 as the barrier, except for two "slits" in y
    thickness = 0.5    # thickness in x-dimension
    slit_center_sep = 1.5  # separation of slit centers in y
    slit_half_width = 0.2  # half the width of each slit in y

    # The "barrier" region is near x=0
    mask_barrier = (np.abs(X) < thickness/2.0)

    # Within that region, let's open two slits in y
    # Slit 1 around y = +slit_center_sep/2, slit 2 around y = -slit_center_sep/2
    slit1 = (Y > (slit_center_sep/2 - slit_half_width)) & (Y < (slit_center_sep/2 + slit_half_width))
    slit2 = (Y > -(slit_center_sep/2 + slit_half_width)) & (Y < -(slit_center_sep/2 - slit_half_width))

    # So the barrier = V0 everywhere in the region mask_barrier, except where slit1 or slit2 is True
    barrier_region = mask_barrier & ~(slit1 | slit2)
    V[barrier_region] = V0

    return V

if __name__ == "__main__":
    main()


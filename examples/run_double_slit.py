
import numpy as np
from src.initialize_system import initialize_system
from src.potential import potential_function
from src.evolve import evolve_wavefunction
from src.visualize import visualize_results_3d

def main():
    print("3D Double-Slit Simulation!")
    print("Enter the following parameters within the specified intervals:\n")

    xmin = float(input("Enter xmin (e.g., -20.0 to -5.0): "))
    while xmin > -5.0 or xmin < -20.0:
        xmin = float(input("Invalid input! Enter xmin in the range -20.0 to -5.0: "))

    xmax = float(input("Enter xmax (e.g., 5.0 to 20.0): "))
    while xmax < 5.0 or xmax > 20.0:
        xmax = float(input("Invalid input! Enter xmax in the range 5.0 to 20.0: "))

    N = int(input("Enter grid size N (e.g., 32 to 128, must be a power of 2): "))
    while not (32 <= N <= 128 and (N & (N - 1)) == 0):
        N = int(input("Invalid input! Enter N in the range 32 to 128 (must be a power of 2): "))

    x0 = float(input("Enter initial wave packet x0 (e.g., xmin < x0 < xmax): "))
    while not (xmin < x0 < xmax):
        x0 = float(input(f"Invalid input! Enter x0 in the range ({xmin}, {xmax}): "))

    sigma = float(input("Enter wave packet width sigma (e.g., 0.5 to 2.0): "))
    while sigma < 0.5 or sigma > 2.0:
        sigma = float(input("Invalid input! Enter sigma in the range 0.5 to 2.0: "))

    V0 = float(input("Enter barrier height V0 (e.g., 10.0 to 50.0): "))
    while V0 < 10.0 or V0 > 50.0:
        V0 = float(input("Invalid input! Enter V0 in the range 10.0 to 50.0: "))

    total_time = float(input("Enter total simulation time (e.g., 0.5 to 10.0): "))
    while total_time < 0.5 or total_time > 10.0:
        total_time = float(input("Invalid input! Enter total_time in the range 0.5 to 10.0: "))

    dt = float(input("Enter time step dt (e.g., 0.001 to 0.05): "))
    while dt < 0.001 or dt > 0.05:
        dt = float(input("Invalid input! Enter dt in the range 0.001 to 0.05: "))

    # Initialize system (3D)
    (X, Y, Z, dx, psi, KX, KY, KZ, dk) = initialize_system(
        xmin, xmax, N, x0, 0.0, 0.0, sigma, 5.0, 0.0, 0.0, hbar=1.0, m=1.0
    )

    # Double-slit potential
    V = double_slit_3d(X, Y, Z, V0)

    # Time evolution
    num_steps = int(total_time / dt)
    for step in range(num_steps):
        psi = evolve_wavefunction(psi, V, dt, dx, KX, KY, KZ, hbar=1.0, m=1.0)

    # Visualize results
    visualize_results_3d(X, Y, psi, step=num_steps, potential=V, z_index=N//2, save_fig=False)
    print("3D Double-Slit Simulation finished.")

def double_slit_3d(X, Y, Z, V0):
    V = np.zeros_like(X)
    thickness = 0.5
    slit_center_sep = 1.5
    slit_half_width = 0.2

    mask_barrier = (np.abs(X) < thickness / 2.0)
    slit1 = (Y > (slit_center_sep / 2 - slit_half_width)) & (Y < (slit_center_sep / 2 + slit_half_width))
    slit2 = (Y > -(slit_center_sep / 2 + slit_half_width)) & (Y < -(slit_center_sep / 2 - slit_half_width))
    barrier_region = mask_barrier & ~(slit1 | slit2)
    V[barrier_region] = V0
    return V

if __name__ == "__main__":
    main()


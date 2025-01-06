"""
Interactive 3D Barrier Potential Simulation.
"""

import numpy as np
from src.initialize_system import initialize_system
from src.potential import potential_function
from src.evolve import evolve_wavefunction
from src.visualize import visualize_results_3d

def main():
    print("Welcome to the 3D Barrier Potential Simulation!")

    # Prompt user for simulation parameters
    xmin = float(input("Enter xmin (e.g., -10.0): "))
    xmax = float(input("Enter xmax (e.g., 10.0): "))
    N = int(input("Enter grid size N (e.g., 64): "))
    x0 = float(input("Enter initial wave packet x0 (e.g., -5.0): "))
    y0 = float(input("Enter initial wave packet y0 (e.g., 0.0): "))
    z0 = float(input("Enter initial wave packet z0 (e.g., 0.0): "))
    sigma = float(input("Enter wave packet width sigma (e.g., 1.0): "))
    kx0 = float(input("Enter initial momentum kx0 (e.g., 3.0): "))
    ky0 = float(input("Enter initial momentum ky0 (e.g., 0.0): "))
    kz0 = float(input("Enter initial momentum kz0 (e.g., 0.0): "))
    V0 = float(input("Enter barrier height V0 (e.g., 10.0): "))
    a = float(input("Enter barrier half-width a (e.g., 1.0): "))
    total_time = float(input("Enter total simulation time (e.g., 2.0): "))
    dt = float(input("Enter time step dt (e.g., 0.01): "))

    # Initialize system
    (X, Y, Z, dx, psi, KX, KY, KZ, dk) = initialize_system(
        xmin, xmax, N, x0, y0, z0, sigma, kx0, ky0, kz0, hbar=1.0, m=1.0
    )

    # Define potential
    V = potential_function(X, Y, Z, potential_type='barrier', V0=V0, a=a)

    # Time evolution
    num_steps = int(total_time / dt)
    for step in range(num_steps):
        psi = evolve_wavefunction(psi, V, dt, dx, KX, KY, KZ, hbar=1.0, m=1.0)

    # Visualize results
    visualize_results_3d(X, Y, psi, step=num_steps, potential=V, z_index=N//2, save_fig=False)
    print("Simulation finished!")

if __name__ == "__main__":
    main()


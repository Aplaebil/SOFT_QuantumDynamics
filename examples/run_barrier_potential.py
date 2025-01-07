import numpy as np
from src.initialize_system import initialize_system
from src.potential import potential_function
from src.evolve import evolve_wavefunction
from src.visualize import visualize_results_3d

def main():
    print("3D Barrier Potential Simulation")
    print("Enter the following parameters within the specified intervals:\n")

    # Prompt user for simulation parameters with intervals
    xmin = float(input("Enter xmin (e.g., -20.0 to -5.0): "))
    while xmin > -5.0 or xmin < -20.0:
        xmin = float(input("Invalid input! Enter xmin in the range -20.0 to -5.0: "))

    xmax = float(input("Enter xmax (e.g., 5.0 to 20.0): "))
    while xmax < 5.0 or xmax > 20.0:
        xmax = float(input("Invalid input! Enter xmax in the range 5.0 to 20.0: "))

    N = int(input("Enter grid size N (e.g., 32 to 128, must be a power of 2): "))
    while not (32 <= N <= 128 and (N & (N - 1)) == 0):  # Power of 2 check
        N = int(input("Invalid input! Enter N in the range 32 to 128 (must be a power of 2): "))

    x0 = float(input("Enter initial wave packet x0 (e.g., xmin < x0 < xmax): "))
    while not (xmin < x0 < xmax):
        x0 = float(input(f"Invalid input! Enter x0 in the range ({xmin}, {xmax}): "))

    y0 = float(input("Enter initial wave packet y0 (e.g., -5.0 to 5.0): "))
    while y0 < -5.0 or y0 > 5.0:
        y0 = float(input("Invalid input! Enter y0 in the range -5.0 to 5.0: "))

    z0 = float(input("Enter initial wave packet z0 (e.g., -5.0 to 5.0): "))
    while z0 < -5.0 or z0 > 5.0:
        z0 = float(input("Invalid input! Enter z0 in the range -5.0 to 5.0: "))

    sigma = float(input("Enter wave packet width sigma (e.g., 0.5 to 2.0): "))
    while sigma < 0.5 or sigma > 2.0:
        sigma = float(input("Invalid input! Enter sigma in the range 0.5 to 2.0: "))

    kx0 = float(input("Enter initial momentum kx0 (e.g., -10.0 to 10.0): "))
    while kx0 < -10.0 or kx0 > 10.0:
        kx0 = float(input("Invalid input! Enter kx0 in the range -10.0 to 10.0: "))

    ky0 = float(input("Enter initial momentum ky0 (e.g., -10.0 to 10.0): "))
    while ky0 < -10.0 or ky0 > 10.0:
        ky0 = float(input("Invalid input! Enter ky0 in the range -10.0 to 10.0: "))

    kz0 = float(input("Enter initial momentum kz0 (e.g., -10.0 to 10.0): "))
    while kz0 < -10.0 or kz0 > 10.0:
        kz0 = float(input("Invalid input! Enter kz0 in the range -10.0 to 10.0: "))

    V0 = float(input("Enter barrier height V0 (e.g., 0.0 to 50.0): "))
    while V0 < 0.0 or V0 > 50.0:
        V0 = float(input("Invalid input! Enter V0 in the range 0.0 to 50.0: "))

    a = float(input("Enter barrier half-width a (e.g., 0.1 to 5.0): "))
    while a < 0.1 or a > 5.0:
        a = float(input("Invalid input! Enter a in the range 0.1 to 5.0: "))

    total_time = float(input("Enter total simulation time (e.g., 0.5 to 10.0): "))
    while total_time < 0.5 or total_time > 10.0:
        total_time = float(input("Invalid input! Enter total_time in the range 0.5 to 10.0: "))

    dt = float(input("Enter time step dt (e.g., 0.001 to 0.05): "))
    while dt < 0.001 or dt > 0.05:
        dt = float(input("Invalid input! Enter dt in the range 0.001 to 0.05: "))

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


import numpy as np
import matplotlib.pyplot as plt

def visualize_results_3d(X, Y, psi, step, potential=None, z_index=None, save_fig=False):

    N = psi.shape[0]  # assume Nx=Ny=Nz
    if z_index is None:
        z_index = N // 2  # pick central slice

    # Probability density slice
    psi_slice = psi[:, :, z_index]
    prob_density = np.abs(psi_slice)**2

    plt.figure(figsize=(6,5))
    plt.title(f"3D Wavefunction Slice (z_index={z_index}) at step {step}")

    # Show probability density
    # X_2d, Y_2d can be extracted:
    X_2d = X[:, :, z_index]
    Y_2d = Y[:, :, z_index]

    # Instead of X_2d, Y_2d, we can display prob_density with imshow
    # but we have to define extent if we want real coordinates on axes:
    x_min, x_max = X_2d[0,0], X_2d[-1,-1]
    y_min, y_max = Y_2d[0,0], Y_2d[-1,-1]

    plt.imshow(prob_density.T, origin='lower',
               extent=[x_min, x_max, y_min, y_max],
               cmap='viridis', aspect='equal')
    plt.colorbar(label='|psi|^2')

    # Overlay potential if provided
    if potential is not None:
        V_slice = potential[:, :, z_index]
        V_min, V_max = np.min(V_slice), np.max(V_slice)
        if V_max > 1e-10:  # to avoid dividing by zero
            # We can overlay contours:
            levels = np.linspace(V_min, V_max, 5)
            plt.contour(X_2d, Y_2d, V_slice, levels=levels, colors='red', alpha=0.5)

    plt.xlabel('x')
    plt.ylabel('y')

    if save_fig:
        plt.savefig(f"wavefunction_3d_step_{step:04d}.png")
        plt.close()
    else:
        plt.show()


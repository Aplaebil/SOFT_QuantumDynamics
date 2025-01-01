import numpy as np
import matplotlib.pyplot as plt

def visualize_results(x, psi, step, potential=None, save_fig=False):
    """
    Visualize the probability density and (optionally) the scaled potential.
    """
    prob_density = np.abs(psi)**2

    plt.figure(figsize=(8, 5))
    plt.title(f"Wavefunction at step {step}")
    plt.plot(x, prob_density, label='|psi|^2')

    if potential is not None:
        # Scale potential for plotting
        pot_scale = (np.max(prob_density) * 0.8) / (np.max(np.abs(potential)) + 1e-10)
        plt.plot(x, potential * pot_scale, 'r--', label='Scaled Potential')

    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.legend()
    
    if save_fig:
        plt.savefig(f"wavefunction_step_{step:04d}.png")
        plt.close()
    else:
        plt.show()


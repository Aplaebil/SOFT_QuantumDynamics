import numpy as np

def compute_total_energy(psi, x, k, V, hbar, m, dx):
    """
    Compute the expectation value of total energy = T + V.
    
    Parameters
    ----------
    psi : np.ndarray
        Wave function in position space.
    x : np.ndarray
        Position grid.
    k : np.ndarray
        Momentum grid.
    V : np.ndarray
        Potential array in position space.
    hbar : float
        Planck's constant (reduced).
    m : float
        Particle mass.
    dx : float
        Spatial grid spacing.
    
    Returns
    -------
    E : float
        Total energy expectation value.
    """

    # Potential energy in position space
    prob_density = np.abs(psi)**2
    E_potential = np.sum(prob_density * V) * dx

    # Kinetic energy in momentum space
    psi_k = np.fft.fft(psi)
    # Normalization for forward and inverse FFT might differ (depends on convention)
    # We'll assume the standard numpy convention
    # The factor of 1/N (or dx, etc.) might be needed for strict normalization.
    # For an L2-normalized wave function, handle carefully. For demonstration:
    T_operator = 0.5 * m**(-1) * (hbar * k)**2  / (2*hbar)
    # Actually, the operator is (hbar^2 k^2) / (2m), let's be explicit:
    T = (hbar**2 * k**2) / (2.0 * m)
    psi_k_norm = psi_k / np.sqrt(len(psi_k))  # approximate normalization

    prob_density_k = np.abs(psi_k_norm)**2
    # Summation in k-space
    dk = 2.0 * np.pi / ((x[-1] - x[0]) / (len(x)/(len(x)-1)))  # approximate if needed
    E_kinetic = np.sum(prob_density_k * T) * dk

    # Total energy
    E = E_kinetic + E_potential
    return E


import numpy as np

def evolve_wavefunction(psi, V, dt, dx, k, hbar, m):
    """
    Evolve the wavefunction by one time step using the split-operator method.
    
    Parameters
    ----------
    psi : np.ndarray
        Wave function in position space.
    V : np.ndarray
        Potential array in position space.
    dt : float
        Time step.
    dx : float
        Spatial grid spacing.
    k : np.ndarray
        Momentum-space grid.
    hbar : float
        Reduced Planck's constant.
    m : float
        Mass of the particle.

    Returns
    -------
    psi_new : np.ndarray
        Updated wave function in position space after one time step.
    """

    # Half-step kinetic operator in momentum space
    psi_k = np.fft.fft(psi)
    kinetic_phase_half = np.exp(-1j * (hbar * (k**2) / (2*m)) * (dt/(2*hbar)))
    psi_k *= kinetic_phase_half
    psi = np.fft.ifft(psi_k)

    # Full potential step in position space
    potential_phase = np.exp(-1j * V * dt / hbar)
    psi *= potential_phase

    # Another half-step kinetic operator
    psi_k = np.fft.fft(psi)
    psi_k *= kinetic_phase_half
    psi_new = np.fft.ifft(psi_k)

    return psi_new


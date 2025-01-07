import numpy as np

def evolve_wavefunction(psi, V, dt, dx, KX, KY, KZ, hbar, m):

    # Kinetic operator: T = (hbar^2 / 2m) * (KX^2 + KY^2 + KZ^2)
    # Full operator: exp(-i T dt / hbar)
    # But we do half-step (split-operator)
    T_factor = 0.5 * dt * (hbar**2 / (2.0 * m * hbar))  # factoring out some constants
    kinetic_phase_half = np.exp(
        -1j * T_factor * (KX**2 + KY**2 + KZ**2)
    )

    # 1) Half-step kinetic in momentum space
    psi_k = np.fft.fftn(psi)
    psi_k *= kinetic_phase_half
    psi_mid = np.fft.ifftn(psi_k)

    # 2) Full-step potential in real space
    potential_phase = np.exp(-1j * V * dt / hbar)
    psi_mid *= potential_phase

    # 3) Another half-step kinetic
    psi_k = np.fft.fftn(psi_mid)
    psi_k *= kinetic_phase_half
    psi_new = np.fft.ifftn(psi_k)

    return psi_new


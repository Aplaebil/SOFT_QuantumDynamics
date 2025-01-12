import numpy as np

def compute_total_energy(psi, V, dx, KX, KY, KZ, hbar, m):

    # 1) Potential energy
    prob_density = np.abs(psi)**2
    volume_element = dx**3  # in 3D
    E_potential = np.sum(prob_density * V) * volume_element

    # 2) Kinetic energy
    #   T = (hbar^2 / 2m)(k_x^2 + k_y^2 + k_z^2)
    #   <T> = ∫ psi*(r) T-operator psi(r) d^3r
    # Implementation: go to momentum space, multiply by T(k).
    psi_k = np.fft.fftn(psi)
    # For standard numpy FFT, no direct 1/N factor ifftn, but wavefunction normalization is tricky. Therefore we write a simple approximate:
    T_of_k = (hbar**2 / (2.0*m)) * (KX**2 + KY**2 + KZ**2)
    # The "prob density" in k-space is |psi_k|^2, though we might need to handle scaling.

    # Weighted sum in k-space with factor dk^3 ~ (2*pi/L)^3
    prob_density_k = np.abs(psi_k)**2
    # The "k-space volume" factor is (2pi / (N dx))^3:
    dk = 2.0 * np.pi / (N * dx)  # approximate spacing in each dimension
    d3k = dk**3

    E_kinetic = np.sum(prob_density_k * T_of_k) * d3k

    # 3) Total energy
    E = E_kinetic + E_potential
    return E


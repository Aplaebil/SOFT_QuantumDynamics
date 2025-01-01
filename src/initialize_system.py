import numpy as np

def initialize_system(xmin, xmax, N, x0, sigma, k0, hbar, m):
    """
    Creates the spatial grid and initializes a Gaussian wave packet.
    
    Parameters
    ----------
    xmin, xmax : float
        Spatial domain boundaries.
    N : int
        Number of grid points (preferably a power of 2).
    x0 : float
        Initial center of the wave packet.
    sigma : float
        Standard deviation of the Gaussian.
    k0 : float
        Initial wave number.
    hbar : float
        Reduced Planck's constant.
    m : float
        Mass of the particle.

    Returns
    -------
    x : np.ndarray
        Spatial grid.
    dx : float
        Spatial step size.
    psi : np.ndarray
        Complex array of the initial wave function in position space.
    k : np.ndarray
        Momentum-space grid (unshifted by default).
    dk : float
        Spacing in the momentum space grid.
    """
    # Spatial grid
    x = np.linspace(xmin, xmax, N, endpoint=False)
    dx = (xmax - xmin) / N

    # Initial Gaussian wave packet
    normalization = (1.0 / (np.pi * sigma**2))**0.25
    psi = normalization * np.exp(-(x - x0)**2 / (2.0 * sigma**2)) * np.exp(1j * k0 * x)

    # Momentum-space grid
    dk = 2.0 * np.pi / (xmax - xmin)
    k = np.fft.fftfreq(N, d=dx) * 2.0 * np.pi

    return x, dx, psi, k, dk


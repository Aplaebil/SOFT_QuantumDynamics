import numpy as np

def initialize_system(
        xmin, xmax, N,
        x0, y0, z0,
        sigma,
        kx0, ky0, kz0,
        hbar, m
    ):
    """
    Creates a 3D spatial grid and initializes a 3D Gaussian wave packet.

    Parameters
    ----------
    xmin, xmax : float
        Spatial domain boundaries for x, y, and z (assuming cube for simplicity).
    N : int
        Number of grid points along each axis (Nx = Ny = Nz = N).
    x0, y0, z0 : float
        Initial center of the wave packet in each dimension.
    sigma : float
        Standard deviation of the Gaussian (assuming same in x, y, z).
    kx0, ky0, kz0 : float
        Initial wave numbers (momenta/hbar) in x, y, z directions.
    hbar : float
        Reduced Planck's constant.
    m : float
        Mass of the particle.

    Returns
    -------
    X, Y, Z : np.ndarray (3D)
        Spatial grids for x, y, z, each shape (N, N, N).
    dx : float
        Spatial step size (dx = dy = dz).
    psi : np.ndarray (3D)
        Complex array of the initial wave function in 3D position space.
    KX, KY, KZ : np.ndarray (3D)
        Momentum-space grids (unshifted by default), each shape (N, N, N).
    dkx : float
        Momentum-space grid spacing in x (dkx = dky = dkz).
    """
    # 1) Spatial grids along each axis
    x = np.linspace(xmin, xmax, N, endpoint=False)
    dx = (xmax - xmin) / N
    # For simplicity, use the same range & step for y, z
    y = x.copy()
    z = x.copy()

    # 2) Create 3D mesh
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')  # shape (N, N, N)

    # 3) 3D Gaussian wave packet
    # psi(r) = A exp[-((x - x0)^2 + (y - y0)^2 + (z - z0)^2) / (2 sigma^2)]
    #          * exp[i(kx0*x + ky0*y + kz0*z)]
    # Normalization: (1 / (sqrt(pi)*sigma))^(3/2) in 3D, approximate
    A = (1.0 / (np.pi**(3/2) * sigma**3))**0.5
    exp_factor = -((X - x0)**2 + (Y - y0)**2 + (Z - z0)**2) / (2.0 * sigma**2)
    plane_wave = 1j * (kx0 * X + ky0 * Y + kz0 * Z)
    psi = A * np.exp(exp_factor) * np.exp(plane_wave)

    # 4) Momentum-space grids
    # For an N-point grid, d(k) = 2pi / (N * dx), but np.fft.fftfreq is simpler:
    k1d = np.fft.fftfreq(N, d=dx) * 2.0 * np.pi  # 1D array of k-values in each dimension
    KX, KY, KZ = np.meshgrid(k1d, k1d, k1d, indexing='ij')  # shape (N, N, N)
    dkx = k1d[1] - k1d[0]  # spacing in k-space (same for x,y,z)

    return X, Y, Z, dx, psi, KX, KY, KZ, dkx


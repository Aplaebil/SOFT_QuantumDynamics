import numpy as np

def initialize_system(
        xmin, xmax, N,
        x0, y0, z0,
        sigma,
        kx0, ky0, kz0,
        hbar, m
    ):

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


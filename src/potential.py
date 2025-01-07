import numpy as np

def potential_function(X, Y, Z, potential_type='free', V0=0.0, a=1.0, m=1.0, omega=1.0):

    if potential_type == 'free':
        # V(r) = 0
        return np.zeros_like(X)

    elif potential_type == 'harmonic':
        # 3D harmonic oscillator: V(r) = 0.5 * m * omega^2 * (x^2 + y^2 + z^2)
        return 0.5 * m * omega**2 * (X**2 + Y**2 + Z**2)

    elif potential_type == 'barrier':
        # 3D "box" barrier: V0 for |x| < a AND |y| < a AND |z| < a
        V = np.zeros_like(X)
        mask = (abs(X) < a) & (abs(Y) < a) & (abs(Z) < a)
        V[mask] = V0
        return V

    elif potential_type == 'sphere':
        # Spherical barrier: radius = a
        # V0 inside sphere, 0 outside (or vice versa)
        V = np.zeros_like(X)
        r2 = X**2 + Y**2 + Z**2
        V[r2 < a**2] = V0
        return V

    else:
        raise ValueError(f"Unknown potential type: {potential_type}")


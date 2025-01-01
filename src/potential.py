import numpy as np

def potential_function(x, potential_type='free', V0=0.0, a=1.0, m=1.0, omega=1.0):
    """
    Returns a 1D potential array for a given potential type.
    
    Parameters
    ----------
    x : np.ndarray
        The position grid.
    potential_type : str
        'free', 'harmonic', 'barrier', 'double_slit', etc.
    V0 : float
        Potential scale (barrier height, etc.).
    a : float
        Characteristic length (barrier half-width, etc.).
    m : float
        Mass, for harmonic oscillator.
    omega : float
        Frequency, for harmonic oscillator.

    Returns
    -------
    V : np.ndarray
        Potential evaluated at each x point.
    """
    if potential_type == 'free':
        return np.zeros_like(x)

    elif potential_type == 'harmonic':
        return 0.5 * m * omega**2 * x**2

    elif potential_type == 'barrier':
        V = np.zeros_like(x)
        mask = np.abs(x) < a
        V[mask] = V0
        return V

    elif potential_type == 'double_slit':
        # Example model: two narrow barriers
        V = np.zeros_like(x)
        slit_width = 0.05
        barrier_width = 0.1
        separation = 0.3

        mask_left = (x > -separation - barrier_width/2) & (x < -separation + barrier_width/2)
        mask_right = (x > separation - barrier_width/2) & (x < separation + barrier_width/2)

        V[mask_left | mask_right] = V0
        return V

    else:
        raise ValueError(f"Unknown potential type: {potential_type}")


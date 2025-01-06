import unittest
import numpy as np
import sys
import os

# Insert the parent directory (the project root) into sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

from src.initialize_system import initialize_system
from src.potential import potential_function
from src.evolve import evolve_wavefunction

class TestEvolve3D(unittest.TestCase):
    def test_evolve_free_particle_3d(self):
        """
        Simple check: if potential is zero in 3D, wave packet should just spread.
        We'll just confirm code runs without error and shapes are valid.
        """
        xmin, xmax = -5.0, 5.0
        N = 32
        x0, y0, z0 = 0.0, 0.0, 0.0
        sigma = 1.0
        kx0, ky0, kz0 = 0.0, 0.0, 0.0
        hbar = 1.0
        m = 1.0
        dt = 0.01
        num_steps = 5

        X, Y, Z, dx, psi, KX, KY, KZ, dkx = initialize_system(
            xmin, xmax, N,
            x0, y0, z0,
            sigma,
            kx0, ky0, kz0,
            hbar, m
        )
        V = potential_function(X, Y, Z, potential_type='free')

        for _ in range(num_steps):
            psi = evolve_wavefunction(psi, V, dt, dx, KX, KY, KZ, hbar, m)

        # Just ensure shape is still (N,N,N) and we didn't crash
        self.assertEqual(psi.shape, (N, N, N))

if __name__ == '__main__':
    unittest.main()


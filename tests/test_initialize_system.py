import unittest
import numpy as np
import sys
import os

# Insert the parent directory (the project root) into sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

from src.initialize_system import initialize_system

class TestInitializeSystem3D(unittest.TestCase):
    def test_initialize_system_shapes_3d(self):
        """
        Check that X, Y, Z, and psi all have the correct 3D shape (N,N,N).
        """
        xmin, xmax = -10.0, 10.0
        N = 64
        x0, y0, z0 = 0.0, 0.0, 0.0
        sigma = 1.0
        kx0, ky0, kz0 = 0.0, 0.0, 0.0
        hbar = 1.0
        m = 1.0

        X, Y, Z, dx, psi, KX, KY, KZ, dkx = initialize_system(
            xmin, xmax, N,
            x0, y0, z0,
            sigma,
            kx0, ky0, kz0,
            hbar, m
        )

        self.assertEqual(X.shape, (N, N, N))
        self.assertEqual(Y.shape, (N, N, N))
        self.assertEqual(Z.shape, (N, N, N))
        self.assertEqual(psi.shape, (N, N, N))
        self.assertEqual(KX.shape, (N, N, N))
        self.assertEqual(KY.shape, (N, N, N))
        self.assertEqual(KZ.shape, (N, N, N))

    def test_wavefunction_normalization_3d(self):
        """
        Check that the initial wavefunction is (approximately) normalized in 3D.
        The normalization integral in 3D is sum(|psi|^2) * dx^3.
        """
        xmin, xmax = -5.0, 5.0
        N = 32
        x0, y0, z0 = 0.0, 0.0, 0.0
        sigma = 1.0
        kx0, ky0, kz0 = 0.0, 0.0, 0.0
        hbar = 1.0
        m = 1.0

        X, Y, Z, dx, psi, KX, KY, KZ, dkx = initialize_system(
            xmin, xmax, N,
            x0, y0, z0,
            sigma,
            kx0, ky0, kz0,
            hbar, m
        )

        prob_density = np.abs(psi)**2
        volume_element = dx**3
        prob = np.sum(prob_density) * volume_element

        # Expect near 1.0
        self.assertAlmostEqual(prob, 1.0, delta=0.01)

if __name__ == '__main__':
    unittest.main()


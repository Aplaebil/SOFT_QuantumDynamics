import unittest
import numpy as np
import sys
import os

# Insert the parent directory (the project root) into sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

from src.potential import potential_function

class TestPotential3D(unittest.TestCase):
    def test_free_potential_3d(self):
        """
        Check that the 'free' potential returns all zeros in 3D.
        """
        N = 32
        x = np.linspace(-5, 5, N, endpoint=False)
        X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
        V = potential_function(X, Y, Z, potential_type='free')
        self.assertTrue(np.allclose(V, 0.0))

    def test_barrier_potential_3d(self):
        """
        Check that the 'barrier' potential is set to V0 inside |x|<a, |y|<a, |z|<a.
        """
        N = 32
        x = np.linspace(-5, 5, N, endpoint=False)
        X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

        V0 = 10.0
        a = 1.0
        V = potential_function(X, Y, Z, potential_type='barrier', V0=V0, a=a)

        # Points where |x|<a, |y|<a, |z|<a should have V=V0
        mask_inside = (abs(X) < a) & (abs(Y) < a) & (abs(Z) < a)
        self.assertTrue(np.all(V[mask_inside] == V0))
        # Outside that region should be 0
        mask_outside = ~mask_inside
        self.assertTrue(np.all(V[mask_outside] == 0))

if __name__ == '__main__':
    unittest.main()


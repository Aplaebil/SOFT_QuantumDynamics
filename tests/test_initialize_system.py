import unittest
import numpy as np
import sys
sys.path.append("../src")
from initialize_system import initialize_system

class TestInitializeSystem(unittest.TestCase):
    def test_initialize_system_shapes(self):
        x, dx, psi, k, dk = initialize_system(-10, 10, 2**8, 0.0, 1.0, 0.0, 1.0, 1.0)
        self.assertEqual(len(x), 2**8)
        self.assertEqual(len(psi), 2**8)
        self.assertEqual(len(k), 2**8)

    def test_wavefunction_normalization(self):
        x, dx, psi, k, dk = initialize_system(-10, 10, 2**8, 0.0, 1.0, 0.0, 1.0, 1.0)
        prob = np.sum(np.abs(psi)**2) * dx
        self.assertAlmostEqual(prob, 1.0, delta=0.01)  # allow small numerical tolerance

if __name__ == '__main__':
    unittest.main()


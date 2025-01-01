import unittest
import numpy as np
import sys
import os

# Insert the parent directory (the project root) into sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

from src.potential import potential_function

class TestPotential(unittest.TestCase):
    def test_free_potential(self):
        x = np.linspace(-5, 5, 101)
        V = potential_function(x, potential_type='free')
        self.assertTrue(np.all(V == 0))

    def test_barrier_potential(self):
        x = np.linspace(-5, 5, 101)
        V0 = 10.0
        a = 1.0
        V = potential_function(x, potential_type='barrier', V0=V0, a=a)
        self.assertTrue(np.any(V != 0))

if __name__ == '__main__':
    unittest.main()


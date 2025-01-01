import unittest
import sys
import os
import numpy as np

# Insert the parent directory (the project root) into sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

from src.visualize import visualize_results

class TestVisualize(unittest.TestCase):
    def test_visualize(self):
        # Just ensure the function runs without error
        x = np.linspace(-5, 5, 101)
        psi = np.exp(-x**2)
        visualize_results(x, psi, step=0, potential=None, save_fig=True)
        # A real test might check if the PNG file was created, etc.

if __name__ == '__main__':
    unittest.main()


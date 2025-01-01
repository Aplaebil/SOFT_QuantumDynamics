import unittest
import sys
sys.path.append("../src")

from visualize import visualize_results
import numpy as np

class TestVisualize(unittest.TestCase):
    def test_visualize(self):
        # Just ensure the function runs without error
        x = np.linspace(-5, 5, 101)
        psi = np.exp(-x**2)
        visualize_results(x, psi, step=0, potential=None, save_fig=True)
        # Check if file got saved would be next step

if __name__ == '__main__':
    unittest.main()


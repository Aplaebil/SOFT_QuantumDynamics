import unittest
import sys
import os
import numpy as np

# Insert the parent directory (the project root) into sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

from src.visualize import visualize_results_3d

class TestVisualize3D(unittest.TestCase):
    def test_visualize_3d(self):
        """
        Ensure the function runs without error for a 3D slice plot.
        """
        # Create a small 3D wavefunction
        N = 16
        x = np.linspace(-5, 5, N, endpoint=False)
        X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
        psi = np.exp(-(X**2 + Y**2 + Z**2))

        # We won't define a real potential here, just a placeholder
        potential = None

        # Just check if we can produce a slice
        # This should create a plot, either show or save.
        # We'll do save_fig=True to avoid an interactive window in some CI environments.
        visualize_results_3d(X, Y, psi, step=0, potential=potential, z_index=N//2, save_fig=True)

if __name__ == '__main__':
    unittest.main()


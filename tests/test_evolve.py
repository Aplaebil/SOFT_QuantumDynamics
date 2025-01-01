import unittest
import numpy as np
import sys
sys.path.append("../src")

from initialize_system import initialize_system
from potential import potential_function
from evolve import evolve_wavefunction

class TestEvolve(unittest.TestCase):
    def test_evolve_free_particle(self):
        # Simple check: if potential is zero, wave packet should just spread
        xmin, xmax = -10, 10
        N = 2**8
        x0 = 0.0
        sigma = 1.0
        k0 = 0.0
        hbar = 1.0
        m = 1.0
        dt = 0.01

        x, dx, psi, k, dk = initialize_system(xmin, xmax, N, x0, sigma, k0, hbar, m)
        V = potential_function(x, potential_type='free')

        # Evolve a few steps
        for _ in range(5):
            psi = evolve_wavefunction(psi, V, dt, dx, k, hbar, m)
        
        # Just ensure code runs; real test would check wave packet broadening, norm, etc.
        self.assertEqual(len(psi), N)

if __name__ == '__main__':
    unittest.main()


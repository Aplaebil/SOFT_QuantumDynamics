# Split-Operator Fourier Transform (SOFT) Method: Project Report

## 1. Introduction

This project demonstrates the **Split-Operator Fourier Transform (SOFT)** method for numerically solving the **time-dependent Schrödinger equation** in one dimension. The SOFT method leverages **operator splitting** and the **Fast Fourier Transform (FFT)** to evolve a wave function under both potential and kinetic energy operators efficiently. While methods like Crank-Nicolson are more commonly taught, SOFT provides a unique blend of conceptual clarity and computational speed, particularly appealing for studying quantum phenomena such as tunneling, wave packet dispersion, and interference.

## 2. Project Overview

The primary goal is to simulate and visualize the **time evolution of a quantum wave packet**. Specifically, we:

1. **Split the Hamiltonian** \(\hat{H}\) into:
   - **Kinetic part**, \(\hat{T}\), acting in momentum space.
   - **Potential part**, \(\hat{V}\), acting in position space.
2. **Approximate the time-evolution operator** \( e^{-i\hat{H}\Delta t/\hbar} \) by sequentially applying partial updates in position and momentum space:
   \[
   e^{-i \hat{H} \Delta t / \hbar}
   \approx
   e^{-i \hat{T} \, \frac{\Delta t}{2\hbar}}
   \; e^{-i \hat{V} \, \frac{\Delta t}{\hbar}}
   \; e^{-i \hat{T} \, \frac{\Delta t}{2\hbar}}.
   \]
3. **Use FFT** to switch between position and momentum space, making it computationally efficient to apply each partial update.

This method’s **key strengths** include its:
- **Flexibility** in handling various potentials.
- **Intuitive visualization** of wave functions in both real (position) and momentum space.
- **Scalability** to higher dimensions if desired.

## 3. Methodology

### 3.1 System Setup

- **Quantum System**: The project considers a **1D time-dependent Schrödinger equation**.  
- **Spatial Discretization**: A finite interval \([x_\mathrm{min}, x_\mathrm{max}]\) is divided into \(N\) grid points.  
- **Initial Wave Function**: Typically, a **Gaussian wave packet** is used:
  \[
  \psi(x,0)
  \;=\;
  A \exp\!\Bigl(-\frac{(x - x_0)^2}{2\sigma^2}\Bigr)\exp\!\bigl(i k_0 x\bigr),
  \]
  where \(x_0\) is the center, \(\sigma\) is the width, and \(k_0\) is the central wave number.

### 3.2 Time Evolution

1. **Hamiltonian Splitting**  
   The Hamiltonian \(\hat{H} = \hat{T} + \hat{V}\) is split into kinetic (\(\hat{T}\)) and potential (\(\hat{V}\)) parts.

2. **Split-Operator Approximation**  
   Each time step \(\Delta t\) is divided so that the kinetic operator acts for half the time step, then the potential operator acts for the full time step, and the kinetic operator acts again for half the time step.

3. **FFT & IFFT**  
   - To apply \(\hat{T}\) in the momentum representation, the wave function \(\psi(x)\) is **Fourier-transformed** into \(\psi(p)\).  
   - The kinetic phase factor \(e^{-i\hat{T}\Delta t/2\hbar}\) is then applied directly as a pointwise multiplication in momentum space.  
   - An **inverse Fourier transform** brings \(\psi(p)\) back to \(\psi(x)\).  
   - The potential phase factor \(e^{-i\hat{V}\Delta t/\hbar}\) is applied as a pointwise multiplication in position space.

### 3.3 Example Potentials
- **Barrier Potential**: A rectangular barrier of height \(V_0\) in the region \(\lvert x \rvert < a\).  
- **Harmonic Oscillator**: \(V(x) = \tfrac12 m \omega^2 x^2\).  
- **Double-Slit Potential**: Multiple slits or apertures for interference experiments.

## 4. Implementation Outline

Even though you have your own code, a typical implementation includes:

1. **Initialization**  
   - Define numerical parameters (\(N\), \(\Delta t\), total simulation time).  
   - Create arrays for \(x\) and momentum \(p\).  
   - Construct the initial wave packet \(\psi(x,0)\).

2. **Potential Definition**  
   - A function `potential_function(x)` that returns \(V(x)\) for the chosen scenario.

3. **Wavefunction Evolution**  
   - A function `evolve_wavefunction(psi, V, dt, ...)` that:
     1. Performs an FFT of \(\psi(x)\).  
     2. Multiplies by the kinetic phase factor in momentum space.  
     3. Performs an IFFT back to position space.  
     4. Multiplies by the potential phase factor in position space.  
     5. Repeats the half-kinetic step again.

4. **Visualization**  
   - Plot \(|\psi(x,t)|^2\) at various time steps to observe wave packet evolution.  
   - Optionally, perform and plot the FFT of \(\psi\) to observe momentum distribution changes over time.

## 5. Results and Observations

Through the project, one can explore:
- **Quantum Tunneling**: A wave packet penetrating a finite potential barrier.  
- **Wave Packet Spreading**: A free particle packet disperses over time.  
- **Harmonic Oscillator**: Observe bound-state oscillations or energy eigenstates.  
- **Interference Patterns**: Double-slit experiments reveal superposition effects.

These simulations illustrate fundamental quantum behavior and reinforce the numerical concepts behind operator splitting and FFT-based methods.

## 6. Potential Extensions

- **Higher Dimensions**: Extend the approach to 2D or 3D for more complex systems.  
- **Different Potentials**: Incorporate time-dependent potentials or interactions for more advanced physics.  
- **Performance Tuning**: Compare the efficiency of SOFT with other numerical methods like Crank-Nicolson.  
- **Validation**: Use analytical solutions (e.g., harmonic oscillator) to gauge numerical accuracy.

## 7. Conclusion

This project provides an effective and visually appealing approach to **simulate and analyze quantum wave packet dynamics**. By splitting the Hamiltonian and leveraging fast Fourier transforms, the SOFT method illustrates how position- and momentum-space updates can be combined for accurate and efficient time evolution. The method is **flexible** (handling various potentials), **straightforward** to implement with Python and NumPy, and **insightful** for understanding core quantum mechanical phenomena.

---

**Recommended Next Steps**  
- Tweak simulation parameters (grid spacing, time step) to find optimal stability and accuracy.  
- Experiment with more exotic potentials (e.g., random or time-dependent) to probe the method’s versatility.  
- Incorporate comparison with analytical results to verify correctness.

**Acknowledgments**  
This report is based on the standard SOFT method framework widely used in computational physics. Special thanks to all contributors of open-source FFT libraries and Python scientific computing tools that make these simulations accessible to everyone.


# Split-Operator Fourier Transform (SOFT) Method: Project Report

## 1. Introduction

This project demonstrates the **Split-Operator Fourier Transform (SOFT)** method for numerically solving the **time-dependent Schrödinger equation**, now extended up to **three dimensions**. The SOFT approach uses operator splitting alongside Fast Fourier Transforms (FFTs) to handle both the kinetic and potential energy updates efficiently. While methods like Crank-Nicolson are frequently used in textbooks, SOFT offers a streamlined workflow, especially handy when visualizing quantum phenomena such as **tunneling**, **wave packet dispersion**, and **multidimensional interference** patterns.

## 2. Project Overview

Our main goal is to **simulate** and **visualize** the evolution of a quantum wave packet in up to three dimensions. Specifically:

- We split the Hamiltonian \(\hat{H}\) into a **kinetic part** \(\hat{T}\) (treated in momentum space) and a **potential part** \(\hat{V}\) (treated in position space).  
- We approximate the time-evolution operator,
  \[
    e^{-i\hat{H}\Delta t/\hbar} \;\approx\;
    e^{-\frac{i\hat{T}\Delta t}{2\hbar}}\;
    e^{-\frac{i\hat{V}\Delta t}{\hbar}}\;
    e^{-\frac{i\hat{T}\Delta t}{2\hbar}},
  \]
  which is the **split-operator** strategy.  
- We use FFTs to switch seamlessly between position and momentum space, making it computationally straightforward to apply each partial update.  

This method’s key strengths include:

- **Flexibility** in handling various potentials (e.g., barriers, harmonic traps, or slits).  
- **Straightforward visualization** of the wavefunction in both real space and momentum space.  
- **Easy scalability** to 2D and 3D, allowing more complex quantum problems to be explored.

## 3. Methodology

### 3.1 System Setup

- **Quantum System**: We consider the **time-dependent Schrödinger equation** in 1D, 2D, or 3D.  
- **Spatial Discretization**: In 3D, for instance, we define a cubic region \([\mathrm{x_{min}}, \mathrm{x_{max}}]\times[\mathrm{y_{min}}, \mathrm{y_{max}}]\times[\mathrm{z_{min}}, \mathrm{z_{max}}]\) and discretize it into a grid of \((N_x \times N_y \times N_z)\) points.  
- **Initial Wavefunction**: Often a **Gaussian wave packet** centered at \((x_0,y_0,z_0)\) with a chosen momentum \((k_{x0}, k_{y0}, k_{z0})\). For 1D, this simply reduces to \(x\)-only grids.

### 3.2 Time Evolution

1. **Hamiltonian Splitting**  
   We write \(\hat{H} = \hat{T} + \hat{V}\).  
   
2. **Split-Operator Approximation**  
   Each time step \(\Delta t\) is applied in three stages:  
   \[
     e^{-\frac{i\hat{T}\Delta t}{2\hbar}},\quad
     e^{-\frac{i\hat{V}\Delta t}{\hbar}},\quad
     e^{-\frac{i\hat{T}\Delta t}{2\hbar}},
   \]
   ensuring we apply **half a kinetic step**, then a **full potential step**, and **another half kinetic step**.

3. **FFT & IFFT**  
   - To apply \(\hat{T}\) (kinetic) in **momentum space**, we **Fourier-transform** the wavefunction \(\psi(\mathbf{x})\) to \(\psi(\mathbf{k})\).  
   - We multiply by the **kinetic phase factor** \(e^{-i\hat{T}\Delta t/(2\hbar)}\) in momentum space.  
   - An **inverse Fourier transform** returns \(\psi(\mathbf{k})\) to \(\psi(\mathbf{x})\).  
   - The potential phase factor \(e^{-i\hat{V}\Delta t/\hbar}\) is applied in **position space** as a pointwise multiplication.

### 3.3 Example Potentials

- **3D Barrier**: A rectangular or cubic barrier of height \(V_0\).  
- **Harmonic Oscillator**: \(V(x,y,z) = \tfrac12 m(\omega^2_x x^2 + \omega^2_y y^2 + \omega^2_z z^2)\).  
- **Double-Slit (2D or 3D)**: More elaborate potential “walls” with slits that mimic the classic interference setup.

## 4. Implementation Outline

**Implementation roadmap**:

1. **Initialization**  
   - Define numerical parameters \((N, \Delta t, \text{total simulation time})\).  
   - Create arrays for position \((x, y, z)\) and momentum \((k_x, k_y, k_z)\).  
   - Construct the initial wavefunction \(\psi(\mathbf{x}, 0)\).  

2. **Potential Definition**  
   - Write a function (e.g., `potential_function(X, Y, Z)`) that returns \(V(\mathbf{x})\) for the chosen scenario.

3. **Wavefunction Evolution**  
   - A function `evolve_wavefunction(psi, V, dt, ...)` that:  
     1. Performs an FFT (or multidimensional FFT) of \(\psi(\mathbf{x})\).  
     2. Multiplies by the **kinetic** phase factor in momentum space.  
     3. IFFT back to position space.  
     4. Multiplies by the **potential** phase factor in position space.  
     5. Repeats the half-kinetic step.  

4. **Visualization**  
   - For **1D**, plot \(|\psi(x,t)|^2\) as a simple line.  
   - For **2D** or **3D**, visualize **2D slices** or **density projections** of \(|\psi(\mathbf{x}, t)|^2\).  
   - Optionally plot \(|\psi(\mathbf{k}, t)|^2\) in momentum space.

## 5. Results and Observations

By running these simulations, we can explore:

- **Quantum Tunneling**: Watch a wave packet encounter and sometimes penetrate a barrier.  
- **Wave Packet Spreading**: A free particle’s Gaussian wavefunction widens over time, emphasizing dispersion.  
- **Harmonic Oscillator**: See classical-like oscillations or examine bound-state modes.  
- **Interference Patterns**: In multi-slit or higher-dimensional setups, interference arises from superposition.

These results illustrate core quantum-mechanical effects and confirm the usefulness of **split-operator** methods with FFT for tackling both 1D and multi-dimensional problems.

## 6. Conclusion

This project highlights a **visually rich** and **conceptually straightforward** way to simulate wavefunction dynamics. By **splitting** the Hamiltonian and using **fast Fourier transforms**, we efficiently handle both kinetic and potential updates. The same code scales from 1D to 3D, offering a broad playground for studying quantum phenomena—whether it’s basic tunneling or high-dimensional interference patterns. This report draws on common references in computational quantum mechanics, with a big thanks to the **Python** community for **NumPy**, **Matplotlib**, and other libraries that enable fast prototyping and stunning visualizations in just a few lines of code.


# **SOFT_QuantumDynamics**

A Python repository that demonstrates how to solve the **time-dependent Schrödinger equation** via the **Split-Operator Fourier Transform (SOFT)** method. Originally developed for 1D systems, it has been extended to **2D/3D** simulations, showcasing phenomena like **quantum tunneling**, **harmonic oscillator**, **double-slit interference**, and more.

---

## **Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [Examples](#examples)
- [Notebooks](#notebooks)
- [Testing](#testing)
- [FAQ / Tips](#faq--tips)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## **Overview**
This project provides a **numerical framework** for studying quantum wave packet evolution under various **potentials** in **1D** or **3D**. Using the **split-operator** approach:
1. We **split** the Hamiltonian into kinetic (\(\hat{T}\)) and potential (\(\hat{V}\)) parts.
2. We apply each part in the **appropriate space** (momentum- vs. position-space) using **Fast Fourier Transforms** (FFT).
3. We repeat these small time steps to observe **wavefunction dynamics** such as tunneling, interference, bound states, etc.

---

## **Features**
- **1D to 3D**: Fully supports 1D simulations; extended code supports multi-dimensional grids (\(x, y, z\)).
- **Potentials**:
  - *Free Particle*
  - *Barrier* (or “box”)
  - *Harmonic Oscillator*
  - *Double-slit* (1D analogy or a 3D version)
- **FFT-based** Kinetic Operator: Efficiently handles the kinetic term in momentum-space.
- **Visualization**:
  - 1D: Probability density vs. position
  - 3D: 2D slices of \(|\psi(x,y,z)|^2\), cross-sections, or contour plots
- **Interactive**: Jupyter notebooks with *ipywidgets* for real-time parameter adjustments.
- **Testing**: A suite of **unit tests** ensuring stable, correct numerical results.

---

## **Project Structure**
A typical directory layout is:

```
SOFT_QuantumDynamics/
├── README.md                  # This file
├── requirements.txt           # Python dependencies
├── LICENSE                    # License file
├── docs/
│   └── report.md              # Additional documentation or write-ups
├── examples/
│   ├── run_barrier_potential.py     # 1D barrier simulation example
│   ├── run_harmonic_oscillator.py   # 1D harmonic oscillator example
│   └── run_double_slit.py           # 1D double-slit interference
├── notebooks/
│   ├── SOFT_demo.ipynb              # Jupyter notebook demo (1D or 3D version)
│   └── interactive_visualization.ipynb  # Interactive sliders for barrier, etc.
├── data/
│   └── results/                # Folder for storing output figures/animations
├── src/
│   ├── __init__.py
│   ├── main.py                 # Default entry point for a quick simulation
│   ├── initialize_system.py    # Creates the spatial (and possibly 3D) grid, wavefunction
│   ├── potential.py            # Defines various potential functions in 1D or 3D
│   ├── evolve.py               # Split-operator evolution (FFT-based)
│   ├── visualize.py            # Plotting routines (1D or 3D)
│   └── utils.py                # Optional: energy calculation, norm checks, etc.
├── tests/
│   ├── test_initialize_system.py
│   ├── test_potential.py
│   ├── test_evolve.py
│   ├── test_visualize.py
│   └── __init__.py
└── .gitignore
```

---

## **Installation**

1. **Clone** this repository:
   ```bash
   git clone https://github.com/your-username/SOFT_QuantumDynamics.git
   cd SOFT_QuantumDynamics
   ```
2. **Set up** a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate    # On macOS/Linux
   # or venv\Scripts\activate  # On Windows
   ```
3. **Install** required packages:
   ```bash
   pip install -r requirements.txt
   ```
   This should include `numpy`, `matplotlib`, and optionally `ipywidgets` for interactive notebooks.

---

## **Quick Start**

- **Run a default 1D simulation**:
  ```bash
  python src/main.py
  ```
  This simulates, by default, a wave packet tunneling through a barrier or something similar, then shows the final plot.

- **Run an example** (e.g., 1D barrier):
  ```bash
  python examples/run_barrier_potential.py
  ```
  This will generate **plots** at intervals and display them.

- **Explore 3D** (if your `src/` is extended to 3D):
  ```bash
  python -m examples.run_barrier_potential_3d
  ```
  or
  ```bash
  python src/main.py
  ```
  if you have changed the default `main.py` for 3D scenarios.

---

## **How It Works**

1. **Initialization**:  
   - We discretize space (1D or 3D) into a uniform grid.  
   - Initialize a **Gaussian wave packet** with given center, width, and momentum.

2. **Hamiltonian Splitting**:
   - The Hamiltonian \( \hat{H} = \hat{T} + \hat{V} \) is split into kinetic and potential operators.
   - **Kinetic step** is done in momentum-space using the FFT, while **potential step** is done in position-space.

3. **Time Evolution**:
   - In each time step \(\Delta t\), we approximate
     \[
       e^{-\tfrac{i}{\hbar}\hat{H}\Delta t}
       \approx
       e^{-\tfrac{i}{2\hbar}\hat{T}\,\Delta t}
       \,e^{-\tfrac{i}{\hbar}\hat{V}\,\Delta t}
       \,e^{-\tfrac{i}{2\hbar}\hat{T}\,\Delta t}.
     \]
   - We repeat for multiple steps to propagate \(\psi\) in time.

4. **Visualization**:
   - **1D**: Plot \(|\psi(x)|^2\) over \(x\).  
   - **3D**: Plot a **2D slice** of \(|\psi(x,y,z)|^2\) or use advanced 3D visualization libraries for volumetric data.

---

## **Examples**

Located in the `examples/` folder:

- **`run_barrier_potential.py`**  
  Demonstrates **tunneling** in 1D. The wave packet partially transmits/reflected by a rectangular barrier.

- **`run_harmonic_oscillator.py`**  
  Shows how a **bound state** wave packet oscillates in the potential well.

- **`run_double_slit.py`**  
  Illustrates **interference** patterns, akin to the classic double-slit experiment.

*(For a 3D version, create or modify scripts with 3D grids, potentials, and calls to 3D methods.)*

---

## **Notebooks**

- **`SOFT_demo.ipynb`**:  
  A step-by-step demonstration (now adapted to 3D if desired) that initializes a wave packet, sets up a potential, and evolves it. Shows final plots.

- **`interactive_visualization.ipynb`**:  
  Uses **ipywidgets** sliders for real-time parameter changes (e.g., barrier height, slit spacing). Great for an interactive understanding of quantum phenomena in either 1D or 3D (with smaller grids).

---

## **Testing**

1. **Run all tests**:
   ```bash
   python -m unittest discover tests
   ```
   This checks correctness of **initialization**, **potential** definitions, **time evolution**, and **visualization**.

2. **Key tests**:
   - `test_initialize_system.py` ensures the wavefunction and grid shapes are correct (1D or 3D).
   - `test_evolve.py` checks that the wavefunction evolves without errors, e.g., for a free particle.
   - `test_potential.py` verifies the potential arrays match expectations (barrier regions, etc.).

---

## **FAQ / Tips**

1. **Performance in 3D**  
   - 3D grids can be large; if you pick \(N=128\) for each dimension, that’s \(128^3 \approx 2\) million points. Consider starting with **smaller** grids (e.g., \(N=32\)) for testing or interactive demos.

2. **Normalization**  
   - Always check your wavefunction is properly normalized (\(\int |\psi|^2 d^3x = 1\)) after initialization and at intervals, especially if you tweak the FFT conventions.

3. **Plotting**  
   - For 3D data, try slicing or advanced libraries (`mayavi`, `ipyvolume`, or `plotly`) for 3D volumetric rendering.

4. **Common Errors**  
   - `ModuleNotFoundError`: Make sure you run `pip install -r requirements.txt` **inside** your virtual environment.  
   - If Python can’t find your modules in `src/`, run scripts from the **project root** or use a `setup.py` “editable install” (`pip install -e .`).

---

## **License**
This project is provided under the terms of the **MIT License** (see [LICENSE](./LICENSE) for details).

---

## **Acknowledgments**
- **NumPy** and **Matplotlib** for core numeric and plotting.
- **ipywidgets** for interactive controls.
- Community resources and tutorials on **FFT-based Schrödinger solvers**.


# **SOFT_QuantumDynamics**

A Python project showcasing how to solve the **time-dependent Schrödinger equation** using the **Split-Operator Fourier Transform (SOFT)** method. Initially designed for **1D** quantum systems, it has since been **expanded** to cover **2D** and **3D** scenarios—letting you explore fascinating effects such as **quantum tunneling**, **harmonic oscillator dynamics**, **double-slit interference**, and beyond.

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

1. **Clone this repo**:
bash
   git clone https://github.com/your-username/SOFT_QuantumDynamics.git
   cd SOFT_QuantumDynamics
   
2. **Create a virtual environment** (recommended):
bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   # or venv\Scripts\activate    # Windows
   
3. **Install dependencies**:
bash
   pip install -r requirements.txt
   
Make sure you have `numpy` and `matplotlib`. If you want the interactive widgets, install `ipywidgets` too.

---

## **Quick Start**

- **Default 1D Run**:
bash
  python src/main.py
  
This runs a simple simulation (e.g., wave packet + barrier), then displays the final wavefunction plot.

- **Run an Example**:
bash
  python examples/run_barrier_potential.py
  
You’ll see wave packet reflection and transmission plotted over time.

- **3D Simulation**:
  If you’ve converted `src/` to 3D, you can do something like:
bash
  python -m examples.run_barrier_potential_3d
  
or adapt `src/main.py` to run a 3D scenario and do:
bash
  python src/main.py
  
---

## **How It Works**

1. **Initialization**:
   - Set up a **spatial grid** (1D or 3D).
   - Define the initial **wave packet** with chosen center, width, and momentum.

2. **Split the Hamiltonian** (\(\hat{H} = \hat{T} + \hat{V}\)):
   - **Kinetic** part is handled in **momentum-space** (FFT).
   - **Potential** part is directly multiplied in **position-space**.

3. **Time Evolution**:
   \[
   e^{-\tfrac{i}{\hbar}\hat{H}\Delta t} 
   \approx 
   e^{-\tfrac{i}{2\hbar}\hat{T}\Delta t} \,
   e^{-\tfrac{i}{\hbar}\hat{V}\Delta t} \,
   e^{-\tfrac{i}{2\hbar}\hat{T}\Delta t}.
   \]
   Repeating this sequence lets us watch the wave packet evolve step by step.

4. **Visualization**:
   - 1D plots of \(|\psi(x)|^2\) vs. \(x\).  
   - 3D data displayed as **2D slices** or advanced volumetric plots.

---

## **Examples**
Inside the `examples/` folder:

- **`run_barrier_potential.py`**:  
  Tunneling through a **rectangular barrier** in 1D.

- **`run_harmonic_oscillator.py`**:  
  Illustrates a **Gaussian wave packet** oscillating in a 1D parabolic well.

- **`run_double_slit.py`**:  
  Demonstrates **interference** patterns reminiscent of the famous double-slit experiment.

Feel free to modify these for **3D** by using the new `initialize_system` and `potential_function` that handle 3D grids.

---

## **Notebooks**
- **`SOFT_demo.ipynb`**:  
  A straightforward tutorial that walks you through setting parameters, evolving the wavefunction, and plotting results. Easily adapted for 3D by adjusting \(N\) and calls to 3D routines.

- **`interactive_visualization.ipynb`**:  
  Take advantage of **ipywidgets** to adjust potential parameters in real time, letting you explore how the wavefunction changes on the fly.

---

## **Testing**
1. **Discover and run all tests**:
bash
   python -m unittest discover tests
   
Ensures that initialization, potential, time evolution, and visualization work correctly.

2. **Highlights**:
   - `test_initialize_system.py`: Checks grid/wavefunction shapes for 1D or 3D.  
   - `test_evolve.py`: Ensures stable time evolution, e.g., free-particle spreading.  
   - `test_potential.py`: Confirms your potential function is correct (barrier regions, etc.).  

---

## **FAQ / Tips**
1. **Large 3D Grids**:  
   - If \(N\) is large in each dimension, you’ll end up with \(N^3\) points—this can get big fast. Start small (\(N=32\) or \(64\)) for demos.

2. **Normalization**:  
   - Always verify \(\int |\psi|^2\,d^3x \approx 1\). Slight deviations occur if you change the FFT normalization or time step.

3. **Common Errors**:  
   - Missing modules? Double-check you’re in the right virtual environment and run `pip install -r requirements.txt`.  
   - Python can’t find local imports? Ensure you’re running scripts from the project root or that you’ve installed the package in editable mode (`pip install -e .`).

---

## **License**
This project is offered under the **MIT License**. See [LICENSE](./LICENSE) for details.

---

## **Acknowledgments**
- **NumPy** and **Matplotlib** for their indispensable numerical and plotting capabilities.
- **ipywidgets** for making interactive quantum explorations a breeze.
- The wider open-source community for tutorials and references on FFT-based Schrödinger solvers.

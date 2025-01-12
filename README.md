# **SOFT_QuantumDynamics**

A Python project showcasing how to solve the **time-dependent Schrödinger equation** using the **Split-Operator Fourier Transform (SOFT)** method. Initially designed for **1D** quantum systems, it has been **expanded** to cover **2D** and **3D** scenarios—letting you explore effects such as **quantum tunneling**, **harmonic oscillator dynamics**, **double-slit interference**, and beyond.

---

## **Table of Contents**
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Examples](#examples)

---

## **Project Structure**
The directory layout is:

```
SOFT_QuantumDynamics/
├── README.md                  # This file
├── requirements.txt           # Python dependencies
├── LICENSE                    # License file
├── docs/
│   └── report.md              # Additional documentn-ups
├── examples/
│   ├── run_barrier_potential.py     # 1D barrier simulation example
│   ├── run_harmonic_oscillator.py   # 1D harmonic oscillator example
│   └── run_double_slit.py           # 1D double-slit interference
├── notebooks/
│   ├── SOFT_demo.ipynb              # Jupyter notebook demo (1D or 3D version)
│   └── interactive_visualization.ipynb  # Interactive sliders for barrier, etc.
├── data/
│   └── results/                # Folder for storing output figu
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
```
git clone https://github.com/your-username/SOFT_QuantumDynamics.git
cd SOFT_QuantumDynamics
```
2. **Virtual environment**:
```
python -m venv venv # Create virtual environment
deactivate # Deactivate virtual environment
```   
3. **Install dependencies**:
```
pip install -r requirements.txt
```
4. **Testing**:
```
export PYTHONPATH=$(pwd) # To include the project root directory (where the src folder resides)
python3 examples/run_barrier_potential.py
python3 examples/run_harmonic_oscillator.py
python3 examples/run_double_slit.py
```   
---


## **Examples**
Inside the `examples/` folder:

- **`run_barrier_potential.py`**:  
  Tunneling through a **rectangular barrier** in 1D.

- **`run_harmonic_oscillator.py`**:  
  Illustrates a **Gaussian wave packet** oscillating in a 1D parabolic well.

- **`run_double_slit.py`**:  
  Demonstrates **interference** patterns reminiscent of the famous double-slit experiment.

---


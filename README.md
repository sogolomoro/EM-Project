# Finite and Infinite Plate Capacitor Simulation

This repository contains Python scripts for simulating the electric field and potential distribution of both finite and infinite parallel plate capacitors. The simulations are performed using the KUEM library, which is designed for solving electrostatic problems numerically.

## Project Description

The project consists of two main scripts:

1. `FinitePlateCapacitor.py`: Simulates a finite parallel plate capacitor with edge effects.

1. `InfinitePlateCapacitor.py`: Simulates an idealized infinite parallel plate capacitor.

The simulations generate visualizations of the electric field, electric potential, and charge density distributions.

## Requirements

To run the scripts, you need the following Python libraries installed:

`numpy`

`matplotlib`

`KUEM` (ensure this library is installed and accessible in your Python environment)

You can install the required libraries using pip:

```bash
pip install numpy matplotlib
```
## How to Run

1. Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/plate-capacitor-simulation.git
cd plate-capacitor-simulation
```

2. Run the Simulations

### Finite Plate Capacitor

To simulate a finite parallel plate capacitor, run the following command:

```bash
python FinitePlateCapacitor.py
```

- You will be prompted to enter:

    - Surface charge density (in integer values).

    - Plate separation distance (in float values). $< 1$

    - Length of the plate (in float values). $<1$

### Infinite Plate Capacitor

To simulate an infinite parallel plate capacitor, run the following command:

```bash
python InfinitePlateCapacitor.py
```

- You will be prompted to enter:

    - Surface charge density (in integer values).

    - Plate separation distance (in float values). $<1$


## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
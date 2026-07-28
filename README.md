# Secure Supply Chain Genetic Algorithm

A modular Genetic Algorithm (GA) for optimizing secure supply chain routing under transportation costs and criminal risks.

## Introduction

This project implements a GA to optimize supply chain distribution models across scaling problem instances where criminal risk and operational costs act as the main optimization variables. 

The model allocates product flows (depicted as weights) from distribution centers i to demand zones j through k possible routes while minimizing:
- Transportation costs
- Route security risks
- Constraint violations

The algorithm explicitly evaluates: 
- Distribution center capacities
- Demand satisfaction
- Alternative route subsections
- Security escort requirements
- Toll costs
- Fuel consumption
- Driver wages
- Variable travel speeds based on route risk
- Minimum shipment sizes
- Maximum transit times

The implementation follows a modular architecture to facilitate experimentation, parameter tuning, and future research extensions.

### Contact & Support
For questions, collaborations, or suggestions, feel free to contact:

**Franco Josué Patiño Morales, M.Sc.**
- Email: franco.jpm@gmail.com

### Citation
If you use this repository or its data instances in academic work, please cite it as follows:

> Franco Josué Patiño Morales. (2026). Secure Supply Chain Genetic Algorithm [GitHub Repository]. https://github.com/FrancoJPM1991/secure-supply-chain-ga.git 

*Related journal article:*
- []

## Optimization Objectives

The fitness function minimizes a weighted objective combining transportation costs, route risks, and constraint penalties:

$$
\text{Fitness} = \alpha \cdot \text{Risk} + \beta \cdot \text{Cost} + \text{Penalties}
$$

Where:
- α: Risk sensitivity weight
- β: Cost sensitivity weight

Penalty functions strictly enforce operational constraints (e.g., capacity limits, transit deadlines).

## Chromosome Structure

Each chromosome consists of a dual-section array representation to manage continuous flow allocations alongside discrete routing decisions:

### 1. Continuous Section ($X_{i,j}$)
Represents the exact shipment weight allocated from distribution center i to demand zone j.

### 2. Integer Section ($\delta_{i,j}$)
Defines the selected operational route indicator:
- `0` = Inactive path
- `1` = Route 1
- `2` = Route 2
- `3` = Route 3

**Total Chromosome Length:**  
2 × (Number of Centers × Number of Demand Zones)

## Evolutionary Operators

- **Selection:** Tournament selection
- **Elitism:** Direct survival of top-performing individual solutions
- **Crossover:** Column-based crossover adapted for matrix structures
- **Mutation:** Adaptive mutation rates scaled by generation progress
- **Constraint Handling:** Integrated repair operator and progressive penalization

## Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/FrancoJPM1991/secure-supply-chain-ga.git 
   cd secure-supply-chain-ga
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Code
Execute the algorithm module from the root folder of the repository:
```bash
python -m src.ga
```
*Note: Problem instances and GA hyperparameters (population size, mutation rates, weights) can be modified directly in `src/config.py`.*

## Repository Structure

### Data Files Directory (`/data/raw/`)
The instances are split into **Small**, **Medium**, and **Large** cases containing the following matrices:
- `distance_...`: Physical distances for each route k.
- `D_...`: Matrix identifying demand requirements at each point j.
- `S_...`: Supply capabilities for each center i.
- `risk_...`: Historic criminal risk probabilities evaluated along route k.
- `tolls_...`: Fixed toll costs associated with route k.
- `Seed_...`: Explicit random seed matrices to guarantee reproducible runs.

```text
secure-supply-chain-ga/
├── data/
│   └── raw/
│       ├── Large/
│       ├── Medium/
│       └── Small/
├── experiments/
│   ├── test_crossover.py
│   ├── test_fitness.py
│   ├── test_ga.py
│   └── ... (modular component unit tests)
├── src/
│   ├── chromosome.py
│   ├── config.py
│   ├── data_loader.py
│   ├── ga.py
│   └── ... (core algorithm mechanics)
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

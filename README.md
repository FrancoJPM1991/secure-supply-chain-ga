# Secure Supply Chain Genetic Algorithm

A modular Genetic algorithm (GA) for optimizing secure supply chain routing under transportation cost and criminal risk

## Introduction

This projects implements a GA to optimize various size increasing cases where criminal risk and cost act as main optmizaion variables. 
The model allocates product flows (depicted as weights) from distribution centers i to demand zones j through k possible routes while minimizing:

- Transportation cost;
- Route security risk;
- Constraint violations.

The algorithm considers: 

- Distribution center capacities;
- Demand satisfaction;
- Alternative route subsections;
- Security escort requirements;
- Toll costs;
- Fuel consumption;
- Driver wages;
- Variable travel speeds based on route risk;
- Minimum shipment sizes;
- Maximum transit times.

The implementation follows a modular architecture to facilitate experimentation and future research. 
Any questions or suggestions? Feel free to contact us:

Franco Josué Patiño Morales, M.Sc.
- franco.jpm@gmail.com.
 
Do you want to use this repository in academic work? Please cite:

- Franco Josué Patiño Morales;
- Secure Supply Chain Genetic Algorithm;
- GitHub repository;
- 2026.

Take a look to the related journal article:

- xxxxxxxxxxxxxxxxxxxxxxxx

## Optimization Objectives

The fitness function combines transportation cost, route risk and penalties:

Fitness = α Risk + β Cost + Penalties

where:

- α = risk weight;
- β = cost weight.

Penalty functions enforce operational constraints

## Chromosome Structure

Each chromosome consists of two sections:

### Continuous section

X(i,j)

Shipment weight from distribution center i to demand zone j.

### Integer section

δ(i,j)

Selected route:

0 = inactive

1 = route 1

2 = route 2

3 = route 3

Total chromosome length:

2 × (Number of centers × Number of demand zones)

## Evolutionary Operators

- Tournament selection;
- Elitism;
- Column-based crossover;
- Adaptive mutation;
- Repair operator;
- Progressive penalization.

## Running

Execute:

python -m src.ga

Problem instances and GA parameters can be modified in src/config.py.

## Repository Structure

### data

- distance_... : distances for each route k;
- D_... : demand of each point j;
- S_... : supply of each point i;
- risk_... : risk associated to each route k;
- tolls_... : tolls associated to each route k;
- Seed_... : seeds used to recreate comparable solutions.

secure-supply-chain-ga/

C:.
|   .gitignore
|   LICENSE
|   README.md
|   requirements.txt
|
+---data
|   \---raw
|       +---Large
|       |       distance_df9C_25D_A.csv
|       |       distance_df9C_25D_B.csv
|       |       distance_df9C_25D_C.csv
|       |       distance_df9C_25D_D.csv
|       |       distance_df9C_25D_E.csv
|       |       D_9C_25D_A.csv
|       |       D_9C_25D_B.csv
|       |       D_9C_25D_C.csv
|       |       D_9C_25D_D.csv
|       |       D_9C_25D_E.csv
|       |       risk_df9C_25D_A.csv
|       |       risk_df9C_25D_B.csv
|       |       risk_df9C_25D_C.csv
|       |       risk_df9C_25D_D.csv
|       |       risk_df9C_25D_E.csv
|       |       Seed_9C_25D.txt
|       |       S_9C_25D_A.csv
|       |       S_9C_25D_B.csv
|       |       S_9C_25D_C.csv
|       |       S_9C_25D_D.csv
|       |       S_9C_25D_E.csv
|       |       tolls_df9C_25D_A.csv
|       |       tolls_df9C_25D_B.csv
|       |       tolls_df9C_25D_C.csv
|       |       tolls_df9C_25D_D.csv
|       |       tolls_df9C_25D_E.csv
|       |
|       +---Medium
|       |       distance_df6C_14D_A.csv
|       |       distance_df6C_14D_B.csv
|       |       distance_df6C_14D_C.csv
|       |       distance_df6C_14D_D.csv
|       |       distance_df6C_14D_E.csv
|       |       D_6C_14D_A.csv
|       |       D_6C_14D_B.csv
|       |       D_6C_14D_C.csv
|       |       D_6C_14D_D.csv
|       |       D_6C_14D_E.csv
|       |       risk_df6C_14D_A.csv
|       |       risk_df6C_14D_B.csv
|       |       risk_df6C_14D_C.csv
|       |       risk_df6C_14D_D.csv
|       |       risk_df6C_14D_E.csv
|       |       Seed_6C_14D.txt
|       |       S_6C_14D_A.csv
|       |       S_6C_14D_B.csv
|       |       S_6C_14D_C.csv
|       |       S_6C_14D_D.csv
|       |       S_6C_14D_E.csv
|       |       tolls_df6C_14D_A.csv
|       |       tolls_df6C_14D_B.csv
|       |       tolls_df6C_14D_C.csv
|       |       tolls_df6C_14D_D.csv
|       |       tolls_df6C_14D_E.csv
|       |
|       \---Small
|               distance_df3C_5D_A.csv
|               distance_df3C_5D_B.csv
|               distance_df3C_5D_C.csv
|               distance_df3C_5D_D.csv
|               distance_df3C_5D_E.csv
|               D_3C_5D_A.csv
|               D_3C_5D_B.csv
|               D_3C_5D_C.csv
|               D_3C_5D_D.csv
|               D_3C_5D_E.csv
|               risk_df3C_5D_A.csv
|               risk_df3C_5D_B.csv
|               risk_df3C_5D_C.csv
|               risk_df3C_5D_D.csv
|               risk_df3C_5D_E.csv
|               Seed_3C_5D.txt
|               S_3C_5D_A.csv
|               S_3C_5D_B.csv
|               S_3C_5D_C.csv
|               S_3C_5D_D.csv
|               S_3C_5D_E.csv
|               tolls_df3C_5D_A.csv
|               tolls_df3C_5D_B.csv
|               tolls_df3C_5D_C.csv
|               tolls_df3C_5D_D.csv
|               tolls_df3C_5D_E.csv
|
+---experiments
|      test_crossover.py
|      test_elitism.py
|      test_fitness.py
|      test_ga.py
|      test_loader.py
|      test_mutation.py
|      test_population.py
|      test_problem.py
|      test_repair.py
|      test_selection.py
|      __init__.py
|   
|   
|
+---results
\---src
       chromosome.py
       config.py
       crossover.py
       data_loader.py
       elitism.py
       fitness.py
       ga.py
       mutation.py
       population.py
       repair.py
       selection.py
       __init__.py
    
    
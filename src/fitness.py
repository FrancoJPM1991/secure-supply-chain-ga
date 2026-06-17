import numpy as np

from src.chromosome import split_chromosome


def evaluate(chromosome, problem, gen=0, n_generations=1):

    D = problem["D"]
    S = problem["S"]

    d = problem["distance"]
    R_comp = problem["risk"]
    C_toll = problem["tolls"]

    centers = problem["centers"]
    demand_zones = problem["demand_zones"]

    n_centers = problem["n_centers"]
    n_demand = problem["n_demand"]

    sub_map = problem["sub_map"]

    x_flat, delta_flat = split_chromosome(chromosome, problem)

    X = np.array(x_flat).reshape((n_centers, n_demand))

    Delta = np.array(delta_flat).reshape((n_centers, n_demand))

    return X, Delta

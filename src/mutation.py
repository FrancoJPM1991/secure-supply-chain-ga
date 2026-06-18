import random
import numpy as np

from src.repair import repair_individual


def mutate(
    individual, problem, indpb=0.05, gen=0, n_generations=1, minimum_shipment_weight=300
):

    ind = individual[:]

    n_centers = problem["n_centers"]
    n_demand = problem["n_demand"]
    n_subsections = problem["n_subsections"]

    D = problem["D"]
    demand_zones = problem["demand_zones"]

    continuous_length = n_centers * n_demand

    decay = 0.1 * (1 - gen / n_generations)

    for i in range(continuous_length):

        if random.random() < indpb:
            j = i % n_demand
            demand_scale = D[demand_zones[j]]
            sigma = demand_scale * 0.3 * decay
            delta_val = np.random.normal(0, sigma)
            ind[i] = max(0, min(ind[i] + delta_val, demand_scale))

    for idx in range(continuous_length, len(ind)):
        if random.random() < indpb / 3:
            ind[idx] = random.randint(0, n_subsections)

    ind = repair_individual(ind, problem, minimum_shipment_weight)

    return ind

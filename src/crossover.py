import random


def crossover(parent1, parent2, problem):

    n_centers = problem["n_centers"]
    n_demand = problem["n_demand"]

    child1 = parent1[:]
    child2 = parent2[:]

    for j in range(n_demand):

        if random.random() < 0.5:

            for i in range(n_centers):

                idx_x = i * n_demand + j

                child1[idx_x] = parent2[idx_x]
                child2[idx_x] = parent1[idx_x]

                idx_delta = n_centers * n_demand + idx_x

                child1[idx_delta] = parent2[idx_delta]
                child2[idx_delta] = parent1[idx_delta]

    return child1, child2

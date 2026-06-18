import random
import numpy as np


def repair_individual(individual, problem, minimum_shipment_weight=300):

    n_centers = problem["n_centers"]
    n_demand = problem["n_demand"]

    D = problem["D"]
    S = problem["S"]

    centers = problem["centers"]
    demand_zones = problem["demand_zones"]
    n_subsections = problem["n_subsections"]

    continuous_len = n_centers * n_demand
    x_flat = individual[:continuous_len]
    X = np.array(x_flat, dtype=float).reshape((n_centers, n_demand))

    delta_flat = individual[continuous_len:]

    Delta = np.array(delta_flat, dtype=int).reshape((n_centers, n_demand))
    # There can't be an individual without active routes
    total_active_routes = np.sum(Delta > 0)
    if total_active_routes == 0:
        for j in range(n_demand):
            if random.random() < 0.7:
                i = random.randint(0, n_centers - 1)
                Delta[i, j] = random.randint(1, n_subsections)
                X[i, j] = max(X[i, j], minimum_shipment_weight)

    # If there is an active route it must have a designated weight
    for i in range(n_centers):
        for j in range(n_demand):
            if Delta[i, j] == 0:
                X[i, j] = 0.0
            elif 0 < X[i, j] < minimum_shipment_weight:
                X[i, j] = minimum_shipment_weight

    # A supply center can't supply more than available stock
    for i in range(n_centers):
        total_supply_from_center = float(np.sum(X[i, :]))
        capacity = S[centers[i]]
        if total_supply_from_center > capacity and total_supply_from_center > 0:
            scale_factor = capacity / total_supply_from_center
            for j in range(n_demand):
                X[i, j] *= scale_factor
                if X[i, j] < minimum_shipment_weight and Delta[i, j] > 0:
                    X[i, j] = minimum_shipment_weight

    # Demand can't be unfullfilled
    for j in range(n_demand):
        total_supply_to_zone = float(np.sum(X[:, j]))
        demand = D[demand_zones[j]]

        if total_supply_to_zone < demand:
            shortfall = demand - total_supply_to_zone
            eligible_centers = []
            for i in range(n_centers):
                center_spare_cap = S[centers[i]] - float(np.sum(X[i, :]))
                if center_spare_cap > 0 and Delta[i, j] > 0:
                    eligible_centers.append((i, center_spare_cap))

            if eligible_centers:
                total_spare = sum(spare for _, spare in eligible_centers)
                for i, spare in eligible_centers:
                    allocation = (
                        shortfall * (spare / total_spare) if total_spare > 0 else 0.0
                    )
                    add = min(allocation, spare)
                    X[i, j] += add
                    if X[i, j] < minimum_shipment_weight and X[i, j] > 0:
                        X[i, j] = minimum_shipment_weight

    # Supply last check
    for i in range(n_centers):
        total_supply = float(np.sum(X[i, :]))
        capacity = S[centers[i]]
        if total_supply > capacity and total_supply > 0:
            scale = capacity / total_supply
            X[i, :] *= scale

    # Individual reassembly
    repaired_ind = X.flatten().tolist() + Delta.flatten().astype(int).tolist()
    return repaired_ind

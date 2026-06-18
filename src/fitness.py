import numpy as np

from src.chromosome import split_chromosome
from src.config import (
    __cached__,
    C_FUEL,
    E_FUEL,
    W_PLUS,
    C_SALARY,
    SECURITY_THRESHOLD,
    C_SEC,
    MAX_CENTERS_PER_ZONE,
    ALPHA,
    BETA,
    MINIMUM_SHIPMENT_WEIGHT,
    MAX_TRANSIT_TIME_HR,
    get_speed,
)


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

    progressive_penalization = max(0.5, gen / n_generations)

    penalty_weights = {
        "under_supply": 1e4 * progressive_penalization,
        "over_supply": 1e3 * progressive_penalization,
        "continuity": 1e3 * progressive_penalization,
        "exceed_demand": 1e3 * progressive_penalization,
        "min_shipment": 1e3 * progressive_penalization,
        "transit_time": 1e3 * progressive_penalization,
        "over_connected": 1e3 * progressive_penalization,
    }

    for i in range(n_centers):
        for j in range(n_demand):
            if Delta[i, j] == 0:
                X[i, j] = 0

    risk = 0
    fuel_cost = 0
    driver_cost = 0
    toll_cost = 0
    sec_cost = 0

    for i in range(n_centers):
        for j in range(n_demand):

            if Delta[i, j] > 0 and X[i, j] > 0:

                d_idx = int(Delta[i, j])

                if d_idx not in sub_map:
                    continue

                subsection = sub_map[d_idx]

                key = (centers[i], demand_zones[j], subsection)

                if key not in d or key not in R_comp or key not in C_toll:
                    continue

                distance = d[key]
                route_risk = R_comp[key]
                toll = C_toll[key]

                fuel_cost += C_FUEL * E_FUEL * (1 + X[i, j] * W_PLUS) * distance

                time_hr = distance / get_speed(route_risk)

                driver_cost += C_SALARY * time_hr

                toll_cost += toll

                risk += route_risk * distance * X[i, j]

                if route_risk > SECURITY_THRESHOLD:
                    sec_cost += C_SEC

    total_cost = fuel_cost + driver_cost + toll_cost + sec_cost

    penalty = 0.0

    # Over connected zones
    for j in range(n_demand):
        active_centers = sum(
            1 for i in range(n_centers) if X[i, j] > 1e-2 and Delta[i, j] > 0
        )
        if active_centers > MAX_CENTERS_PER_ZONE:
            penalty += penalty_weights["over_connected"] * (
                active_centers - MAX_CENTERS_PER_ZONE
            )

    # Demand satisfaction
    for j in range(n_demand):
        demand_satisfied = sum(X[i, j] for i in range(n_centers))
        demand_required = D[demand_zones[j]]
        if demand_satisfied < demand_required:
            shortfall = demand_required - demand_satisfied
            penalty += penalty_weights["under_supply"] * shortfall

    # Supply
    for i in range(n_centers):
        supplied = sum(X[i, j] for j in range(n_demand))
        if supplied > S[centers[i]]:
            penalty += penalty_weights["over_supply"] * abs(supplied - S[centers[i]])

    # Continuity
    for i in range(n_centers):
        for j in range(n_demand):
            if Delta[i, j] == 0 and X[i, j] > 0:
                penalty += penalty_weights["continuity"]

    # Minimum shipment
    for i in range(n_centers):
        for j in range(n_demand):
            if Delta[i, j] > 0 and X[i, j] < MINIMUM_SHIPMENT_WEIGHT:
                shortfall = MINIMUM_SHIPMENT_WEIGHT - X[i, j]
                penalty += penalty_weights["min_shipment"] * shortfall

    # Maximum travel time
    for i in range(n_centers):
        for j in range(n_demand):
            if Delta[i, j] > 0:
                d_idx = int(Delta[i, j])
                if d_idx not in sub_map:
                    continue
                subsection = sub_map[d_idx]
                key = (centers[i], demand_zones[j], subsection)
                if key in R_comp:
                    route_risk = R_comp[(centers[i], demand_zones[j], subsection)]
                    speed = get_speed(route_risk)
                    distance = d[(centers[i], demand_zones[j], subsection)]
                    travel_time = distance / speed
                if travel_time > MAX_TRANSIT_TIME_HR:
                    penalty += penalty_weights["transit_time"] * abs(
                        travel_time - MAX_TRANSIT_TIME_HR
                    )

    # Sparsity incentive
    lambda_sparse = 0 * progressive_penalization
    n_active_routes = sum(
        1
        for i in range(n_centers)
        for j in range(n_demand)
        if X[i, j] >= MINIMUM_SHIPMENT_WEIGHT
    )
    sparsity_penalty = lambda_sparse * n_active_routes

    fitness = ALPHA * risk + BETA * total_cost + penalty + sparsity_penalty

    return (fitness, total_cost, risk, penalty, sparsity_penalty)

import random


def init_individual(problem, minimum_shipment_weight):

    D = problem["D"]
    S = problem["S"]

    centers = problem["centers"]
    demand_zones = problem["demand_zones"]

    n_centers = problem["n_centers"]
    n_demand = problem["n_demand"]

    x_gene = [0.0] * (n_centers * n_demand)
    delta = [0] * (n_centers * n_demand)

    for j in range(n_demand):
        demand_j = D[demand_zones[j]]
        eligible_centers = [i for i in range(n_centers) if S[centers[i]] > 0]
        random.shuffle(eligible_centers)

        remaining_demand = demand_j

        for i in eligible_centers:
            if remaining_demand <= 0:
                break

            center_available_cap = S[centers[i]]
            already_used = sum(x_gene[i * n_demand + idx] for idx in range(n_demand))

            cap_left = center_available_cap - already_used

            if cap_left <= 0:
                continue

            if remaining_demand >= minimum_shipment_weight:
                upper = min(cap_left, remaining_demand)
                low = minimum_shipment_weight

                if upper >= low:
                    assign_amount = random.uniform(low, upper)
                else:
                    continue
            else:
                assign_amount = min(cap_left, remaining_demand)

            x_gene[i * n_demand + j] = assign_amount
            remaining_demand -= assign_amount

            delta[i * n_demand + j] = (
                random.randint(1, 3) if x_gene[i * n_demand + j] > 0 else 0
            )

    return x_gene + delta


def init_population(problem, population_size, minimum_shipment_weight):
    return [
        init_individual(problem, minimum_shipment_weight)
        for _ in range(population_size)
    ]

from src.ga import initialize_ga
from src.ga import create_mating_pool
from src.ga import create_offspring
from src.ga import evaluate_population
from src.config import N_GENERATIONS
from src.ga import generate_children
from src.ga import create_next_generation

results = initialize_ga(population_size=10)

mating_pool = create_mating_pool(
    results["population"], results["fitness_values"], tournament_size=5
)

offspring = create_offspring(mating_pool, results["problem"])

sorted_pop, sorted_fits = evaluate_population(
    results["population"], results["problem"], 0, N_GENERATIONS
)

children = generate_children(
    mating_pool=mating_pool,
    problem=results["problem"],
    cx_prob=1.0,
    mut_prob=0.05,
    gen=0,
    n_generations=N_GENERATIONS,
    minimum_shipment_weight=300,
)

next_population = create_next_generation(
    results["elites"], children, population_size=10
)

print(len(results["population"]))

print(len(results["fitness_values"]))

print(len(results["best_individual"]))

print()

print(results["best_fitness"])

print()

print(len(results["elites"]))

print(len(results["elites"][0]))

print()

print(len(mating_pool))

print(len(mating_pool[0]))

print()

print(len(offspring))

print(len(offspring[0]))

print()

print(len(sorted_pop))

print(len(sorted_fits))

print(sorted_fits[0][0])

print()

print(len(children))

print(len(children[0]))

print()

print(len(next_population))

print(len(next_population[0]))

print("GA initialization passed.")

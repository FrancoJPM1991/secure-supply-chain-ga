from src.data_loader import load_case

from src.population import init_population

from src.crossover import crossover

problem = load_case("large", "E")

population = init_population(problem, population_size=2, minimum_shipment_weight=300)

parent1 = population[0]
parent2 = population[1]

child1, child2 = crossover(parent1, parent2, problem)

print(len(parent1), len(parent2))

print(len(child1), len(child2))

assert len(parent1) == len(child1)
assert len(parent2) == len(child2)

print()

print("Crossover passed.")

print()

print(parent1 == child1)

print(parent2 == child2)

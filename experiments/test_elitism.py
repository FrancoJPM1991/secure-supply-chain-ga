from src.data_loader import load_case
from src.population import init_population
from src.fitness import evaluate
from src.elitism import get_elites

problem = load_case("large", "E")

population = init_population(problem, population_size=10, minimum_shipment_weight=300)

fitness_values = []

for individual in population:
    fitness, *_ = evaluate(individual, problem)
    fitness_values.append(fitness)

elites = get_elites(population, fitness_values, elitism_percentage=0.05)

print("Population size:", len(population))

print("Elite size:", len(elites))

print("Elite chromosome length:", len(elites[0]))

assert len(elites) == 1
assert len(elites[0]) == len(population[0])

print()
print("Elitism passed.")

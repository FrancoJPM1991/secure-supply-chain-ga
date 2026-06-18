from src.data_loader import load_case
from src.population import init_population
from src.mutation import mutate

problem = load_case("large", "E")

population = init_population(problem, population_size=1, minimum_shipment_weight=300)

parent = population[0]

child = mutate(parent, problem, indpb=0.05, gen=0, n_generations=300)

print(len(parent))

print(len(child))

assert len(parent) == len(child)

print()

print(parent == child)

print()

print("Mutation passed.")

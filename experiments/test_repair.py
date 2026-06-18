from src.data_loader import load_case
from src.population import init_population
from src.repair import repair_individual

problem = load_case("large", "E")

population = init_population(problem, population_size=1, minimum_shipment_weight=300)

individual = population[0]

repaired = repair_individual(individual, problem, minimum_shipment_weight=300)

print(len(individual))

print(len(repaired))

assert len(individual) == len(repaired)

print()
print("Repair passed.")

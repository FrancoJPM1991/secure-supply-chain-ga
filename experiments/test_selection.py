from src.data_loader import load_case
from src.population import init_population
from src.fitness import evaluate
from src.selection import tournament_selection

# Load problem
problem = load_case("large", "E")

# Generate population
population = init_population(problem, population_size=10, minimum_shipment_weight=300)

# Evaluate population
fitness_values = []

for individual in population:
    fitness, *_ = evaluate(individual, problem)
    fitness_values.append(fitness)

# Tournament selection
winner = tournament_selection(population, fitness_values, tournament_size=5)

print("Population:", len(population))
print("Fitness values:", len(fitness_values))

print()
print("Winner chromosome length:", len(winner))
print("Expected:", len(population[0]))

from src.data_loader import load_case
from src.population import init_individual, init_population

from src.chromosome import chromosome_length, split_chromosome

problem = load_case("large", "E")

chromosome = init_individual(problem, minimum_shipment_weight=500)

x, delta = split_chromosome(chromosome, problem)

population = init_population(problem, population_size=20, minimum_shipment_weight=500)

print("Chromosome length:", chromosome_length(problem))

print("Population size:", len(population))

print("First individual length:", len(population[0]))

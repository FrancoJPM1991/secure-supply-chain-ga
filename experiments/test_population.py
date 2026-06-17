from src.data_loader import load_case
from src.population import init_individual

problem = load_case("large", "E")

chromosome = init_individual(problem, minimum_shipment_weight=500)

n = problem["n_centers"] * problem["n_demand"]

x = chromosome[:n]
delta = chromosome[n:]

violations = 0

for shipment, subsection in zip(x, delta):
    if shipment > 0 and subsection == 0:
        violations += 1
    if shipment == 0 and subsection != 0:
        violations += 1

print()
print("Consistency violations:", violations)

print("Chromosome length:", len(chromosome))
print("X nonzero genes:", sum(v > 0 for v in x))
print("Delta active genes:", sum(v > 0 for v in delta))

print()
print("First 10 X genes:")
print(x[:10])

print()
print("First 10 Delta genes:")
print(delta[:10])

assert violations == 0

assert len(chromosome) == (2 * problem["n_centers"] * problem["n_demand"])

assert sum(v > 0 for v in x) == sum(v > 0 for v in delta)

print()
print("All population tests passed.")

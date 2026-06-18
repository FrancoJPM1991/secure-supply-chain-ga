from src.data_loader import load_case
from src.population import init_individual
from src.fitness import evaluate

problem = load_case("large", "E")

chromosome = init_individual(problem, minimum_shipment_weight=300)

fitness, total_cost, risk, penalty, sparsity_penalty = evaluate(chromosome, problem)

print("Fitness:", fitness)
print()

print("Cost:", total_cost)
print("Risk:", risk)
print("Penalty:", penalty)
print("Sparsity:", sparsity_penalty)

assert fitness >= 0
assert total_cost >= 0
assert risk >= 0
assert penalty >= 0

print()
print("Fitness evaluation passed.")

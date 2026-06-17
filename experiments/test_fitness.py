from src.data_loader import load_case
from src.population import init_individual
from src.fitness import evaluate
from src.config import get_speed

problem = load_case("large", "E")

chromosome = init_individual(problem, minimum_shipment_weight=500)

X, Delta = evaluate(chromosome, problem)

print(X.shape)
print(Delta.shape)

print(get_speed(0.2))
print(get_speed(0.5))
print(get_speed(0.8))

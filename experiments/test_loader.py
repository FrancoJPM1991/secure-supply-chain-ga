from src.data_loader import load_case

data = load_case("large", "E")

print("Demand:", data["D"])
print("Demand total:", sum(data["D"].values()))

print()

print("Supply:", data["S"])
print("Supply total:", sum(data["S"].values()))

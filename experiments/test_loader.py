from src.data_loader import load_case

data = load_case("large", "E")

print("Demand total:", sum(data["D"].values()))
print("Supply total:", sum(data["S"].values()))

print()

print("Distance entries:", len(data["distance"]))

print()

print(data["distance_df"].head())

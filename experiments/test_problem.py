from src.data_loader import load_case

problem = load_case("large", "E")

print("Centers:", problem["n_centers"])
print("Demand zones:", problem["n_demand"])
print("Subsections:", problem["n_subsections"])

print()

print("First center:", problem["centers"][0])
print("First zone:", problem["demand_zones"][0])

print()

print("Demand Zone1:", problem["D"]["Zone1"])
print("Supply DC1:", problem["S"]["DC1"])

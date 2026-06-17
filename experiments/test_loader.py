from src.data_loader import load_case

D = load_case("large", "E")

print(D)
print(sum(D.values()))

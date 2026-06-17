from src.data_loader import load_case

files = load_case("large", "E")

for key, value in files.items():
    print(f"{key}: {value}")
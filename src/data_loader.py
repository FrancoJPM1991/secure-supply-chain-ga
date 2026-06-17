import pandas as pd
import csv


def load_case(size, subcase):
    """
    Function used to un-package data from raw .csv
    :param size: "small", "medium", "large"
    :param subcase: "A", "B", "C", "D", "E"
    :return:
    """
    size_map = {"small": "3C_5D", "medium": "6C_15D", "large": "9C_25D"}

    problem_size = size_map[size]

    base_path = f"data/raw/{size}"

    demand_file = f"{base_path}/D_{problem_size}_{subcase}.csv"
    supply_file = f"{base_path}/S_{problem_size}_{subcase}.csv"

    distance_file = f"{base_path}/distance_df{problem_size}_{subcase}.csv"
    risk_file = f"{base_path}/risk_df{problem_size}_{subcase}.csv"
    tolls_file = f"{base_path}/tolls_df{problem_size}_{subcase}.csv"

    with open(demand_file, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        values = next(reader)
        D = dict(zip(headers, values))
    D = {key: int(float(value)) for key, value in D.items()}

    with open(supply_file, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        values = next(reader)
        S = dict(zip(headers, values))

    S = {key: int(float(value)) for key, value in S.items()}

    distances_df = pd.read_csv(distance_file)

    if "Unnamed: 0" in distances_df.columns:
        distances_df = distances_df.drop(columns=["Unnamed: 0"])

    d = {
        (row["Center"], row["DemandZone"], row["Subsection"]): row["Distance_km"]
        for _, row in distances_df.iterrows()
    }

    centers = list(distances_df["Center"].unique())
    demand_zones = list(distances_df["DemandZone"].unique())
    subsections = sorted({k[2] for k in d.keys()})

    n_centers = len(centers)
    n_demand = len(demand_zones)
    n_subsections = len(subsections)

    sub_map = {idx + 1: sub for idx, sub in enumerate(subsections)}

    risks_df = pd.read_csv(risk_file)

    if "Unnamed: 0" in risks_df.columns:
        risks_df = risks_df.drop(columns=["Unnamed: 0"])

    R_comp = {
        (row["Center"], row["DemandZone"], row["Subsection"]): row["CompositeRisk"]
        for _, row in risks_df.iterrows()
    }

    return {
        "D": D,
        "S": S,
        "distance_df": distances_df,
        "distance": d,
        "risk_df": risks_df,
        "risk": R_comp,
        "centers": centers,
        "demand_zones": demand_zones,
        "subsections": subsections,
        "n_centers": n_centers,
        "n_demand": n_demand,
        "n_subsections": n_subsections,
        "sub_map": sub_map,
    }

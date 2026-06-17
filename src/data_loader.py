import pandas as pd
import csv

def load_case(size, subcase):
    """
    Function used to un-package data from raw .csv
    :param size: "small", "medium", "large"
    :param subcase: "A", "B", "C", "D", "E"
    :return:
    """
    size_map = {
        "small": "3C_5D",
        "medium": "6C_15D",
        "large": "9C_25D"
    }

    problem_size = size_map[size]

    base_path = f"data/raw/{size}"

    demand_file = f"{base_path}/D_{problem_size}_{subcase}.csv"
    supply_file = f"{base_path}/S_{problem_size}_{subcase}.csv"

    distance_file = f"{base_path}/distance_df{problem_size}_{subcase}.csv"
    risk_file = f"{base_path}/risk_df{problem_size}_{subcase}.csv"
    tolls_file = f"{base_path}/tolls_df{problem_size}_{subcase}.csv"

    return {
        "demand": demand_file,
        "supply": supply_file,
        "distance": distance_file,
        "risk": risk_file,
        "tolls": tolls_file
    }

    # with open(f"{case_path}/D.csv", "r") as f:
    #     reader = csv.reader(f)
    #     headers = next(reader)
    #     values = next(reader)
    #     D = dict(zip(headers, values))
    # D = {key: int(float(value)) for key, value in D.items()}
    #
    # with open(f"{case_path}/S.csv", "r") as f:
    #     reader = csv.reader(f)
    #     headers = next(reader)
    #     values = next(reader)
    #     S = dict(zip(headers, values))
    # S = {key: int(float(value)) for key, value in S.items()}
    #
    # return D, S
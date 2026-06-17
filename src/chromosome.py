def split_chromosome(chromosome, problem):

    n = problem["n_centers"] * problem["n_demand"]

    x = chromosome[:n]
    delta = chromosome[n:]

    return x, delta


def chromosome_length(problem):

    return 2 * problem["n_centers"] * problem["n_demand"]

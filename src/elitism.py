def get_elites(population, fitness_values, elitism_percentage):
    n_elites = max(1, int(len(population) * elitism_percentage))

    ranked = sorted(range(len(population)), key=lambda i: fitness_values[i])

    elites = [population[i][:] for i in ranked[:n_elites]]

    return elites

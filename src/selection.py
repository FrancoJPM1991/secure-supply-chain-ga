import random


def tournament_selection(population, fitness_values, tournament_size):

    participants = random.sample(range(len(population)), tournament_size)

    winner = min(participants, key=lambda i: fitness_values[i])

    return population[winner]

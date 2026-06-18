from src.data_loader import load_case
from src.population import init_population
from src.fitness import evaluate
from src.elitism import get_elites
from src.selection import tournament_selection
from src.crossover import crossover
from src.mutation import mutate
from src.repair import repair_individual
import random
from copy import deepcopy
import numpy as np
from src.config import *


def initialize_ga(
    case_size="large", case_variant="E", population_size=10, minimum_shipment_weight=300
):
    problem = load_case(case_size, case_variant)
    population = init_population(problem, population_size, minimum_shipment_weight)

    fitness_values = []

    for individual in population:
        fitness, *_ = evaluate(individual, problem)
        fitness_values.append(fitness)

    elites = get_elites(population, fitness_values, elitism_percentage=0.05)

    best_idx = min(range(len(population)), key=lambda i: fitness_values[i])
    best_individual = population[best_idx]
    best_fitness = fitness_values[best_idx]

    return {
        "problem": problem,
        "population": population,
        "fitness_values": fitness_values,
        "best_individual": best_individual,
        "best_fitness": best_fitness,
        "elites": elites,
    }


def create_mating_pool(population, fitness_values, tournament_size=5):

    mating_pool = []
    for _ in range(len(population)):
        parent = tournament_selection(population, fitness_values, tournament_size)
        mating_pool.append(parent)
    return mating_pool


def create_offspring(mating_pool, problem):
    offspring = []
    for i in range(0, len(mating_pool), 2):
        parent1 = mating_pool[i]

        parent2 = mating_pool[(i + 1) % len(mating_pool)]

        child1, child2 = crossover(parent1, parent2, problem)
        offspring.append(child1)
        offspring.append(child2)

    return offspring[: len(mating_pool)]


def evaluate_population(population, problem, gen, n_generations):
    fits = [evaluate(ind, problem, gen, n_generations) for ind in population]
    sorted_pairs = sorted(zip(population, fits), key=lambda x: x[1][0])
    sorted_pop = [ind for ind, _ in sorted_pairs]
    sorted_fits = [f for _, f in sorted_pairs]

    return sorted_pop, sorted_fits


def generate_children(
    mating_pool,
    problem,
    cx_prob,
    mut_prob,
    gen,
    n_generations,
    minimum_shipment_weight=300,
):
    children = []

    for i in range(0, len(mating_pool) - 1, 2):
        p1 = deepcopy(mating_pool[i])
        p2 = deepcopy(mating_pool[i + 1])

        if random.random() < cx_prob:
            c1, c2 = crossover(p1, p2, problem)
            c1 = repair_individual(c1, problem, minimum_shipment_weight)
            c2 = repair_individual(c2, problem, minimum_shipment_weight)
        else:
            c1 = p1
            c2 = p2

        children.append(
            mutate(c1, problem, mut_prob, gen, n_generations, minimum_shipment_weight)
        )
        children.append(
            mutate(c2, problem, mut_prob, gen, n_generations, minimum_shipment_weight)
        )

    if len(mating_pool) % 2 != 0:
        p = deepcopy(mating_pool[-1])
        children.append(
            mutate(p, problem, mut_prob, gen, n_generations, minimum_shipment_weight)
        )

    return children


def create_next_generation(elites, children, population_size):
    n_elites = len(elites)

    next_population = elites + children[: population_size - n_elites]

    return next_population


def run_ga():

    state = initialize_ga(
        case_size="small",
        case_variant="A",
        population_size=POP_SIZE,
        minimum_shipment_weight=MINIMUM_SHIPMENT_WEIGHT,
    )

    problem = state["problem"]
    population = state["population"]

    logbook = []
    bests = []

    best_score = state["best_fitness"]
    best_ind_ever = deepcopy(state["best_individual"])
    best_fit_ever = state["best_fitness"]
    best_gen = 0

    for gen in range(N_GENERATIONS):

        sorted_pop, sorted_fits = evaluate_population(
            population, problem, gen, N_GENERATIONS
        )
        elites = get_elites(sorted_pop, sorted_fits, ELITISM_PERCENTAGE)
        penalty = sorted_fits[0][3] if len(sorted_fits) > 0 else 0
        cx_prob = (
            CROSSOVER_PROBABILITY[1] if penalty > 1e-3 else CROSSOVER_PROBABILITY[0]
        )
        mut_prob = max(
            MUTATION_PROBABILITY[0], MUTATION_PROBABILITY[1] * (1 - gen / N_GENERATIONS)
        )
        fitness_values = [f[0] for f in sorted_fits]
        mating_pool = create_mating_pool(
            population, fitness_values, TOURNAMENT_PARTICIPANTS
        )

        children = generate_children(
            mating_pool,
            problem,
            cx_prob,
            mut_prob,
            gen,
            N_GENERATIONS,
            MINIMUM_SHIPMENT_WEIGHT,
        )
        population = create_next_generation(elites, children, POP_SIZE)
        fits = [evaluate(ind, problem, gen, N_GENERATIONS) for ind in population]
        fitness_values = [f[0] for f in fits]
        avg_fitness = np.mean(fitness_values)
        min_fitness = np.min(fitness_values)
        best_idx = np.argmin(fitness_values)
        best_fit_pre = (population[best_idx], fits[best_idx])
        fitness, total_cost, risk, penalty, sparsity = best_fit_pre[1]
        logbook.append((gen, fitness, avg_fitness, total_cost, risk, penalty))
        bests.append((total_cost, risk))

        if fitness < best_score:
            best_score = fitness
            best_ind_ever = deepcopy(best_fit_pre[0])
            best_fit_ever = best_fit_pre[1]
            best_gen = gen

        if gen % 10 == 0 or gen == N_GENERATIONS - 1:
            print(
                f"Gen {gen:3d}: Fitness = {fitness:8.2f}, Cost = ${total_cost:8.2f}, "
                f"Risk = {risk:8.2f}, Penalty = {penalty:6.2f}"
            )

    print(f"\n- Final Best Solution Found in Generation: {best_gen}")
    print(f"- Best Fitness: {best_score:.2f}")

    return (population, logbook, bests, best_ind_ever, best_fit_ever)


if __name__ == "__main__":

    print("Starting GA...")

    population, logbook, bests, best_ind, best_fit = run_ga()

    print()

    print("GA finished.")

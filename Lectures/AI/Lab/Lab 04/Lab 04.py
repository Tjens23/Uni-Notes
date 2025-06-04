import random
import queens_fitness
import time
import math
p_mutation = 0.2
num_of_generations = 10000  # Increased for n-queens problem


def get_fittest_individual(population, fitness_fn):
    return max(population, key=fitness_fn)


def genetic_algorithm(population, fitness_fn, n_queens):
    """Modified to use n_queens as target rather than minimal_fitness"""
    max_fitness = (n_queens * (n_queens - 1)) // 2 # Maximum non-conflicting pairs
    print(f"Max fitness for {n_queens}-queens problem: {max_fitness}")
    for generation in range(num_of_generations):
        print(f"Generation {generation}:")
        print_population(population, fitness_fn)

        new_population = set()

        # Generate twice as many children to account for crossover producing two offspring
        for i in range(len(population) // 2):
            mother, father = random_selection(population, fitness_fn)
            child1, child2 = reproduce_queens(mother, father)

            if random.uniform(0, 1) < p_mutation:
                child1 = mutate_queens(child1, n_queens)
            if random.uniform(0, 1) < p_mutation:
                child2 = mutate_queens(child2, n_queens)

            new_population.add(child1)
            new_population.add(child2)

        # Merge and trim the population to keep the best individuals only
        combined_population = population.union(new_population)
        # Sort by fitness descending
        sorted_population = sorted(combined_population, key=fitness_fn, reverse=True)
        # Trim to fixed population size
        population = set(sorted_population[:len(population)])

        fittest_individual = get_fittest_individual(population, fitness_fn)

        # Check if we've found a solution with no conflicts
        if fitness_fn(fittest_individual) == max_fitness:
            break

    print(f"Final generation {generation}:")
    print_population(population, fitness_fn)

    return fittest_individual

def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))



def reproduce_queens(mother, father):
    """Modified reproduction to handle queens representation and return two children"""
    crossover_point = random.randint(1, len(mother) - 1)
    child1 = list(mother[:crossover_point]) + list(father[crossover_point:])
    child2 = list(father[:crossover_point]) + list(mother[crossover_point:])
    return tuple(child1), tuple(child2)

def mutate_queens(individual, n_queens):
    """Modified mutation for queens - randomly choose a position and change its row"""
    bit_list = list(individual)
    index_to_flip = random.randint(0, len(bit_list) - 1)
    bit_list[index_to_flip] = random.randint(1, 8)
    return tuple(bit_list)



def random_selection(population, fitness_fn):
    """Modified to handle negative fitness values or zero total fitness"""
    # Get fitness values
    fitness_values = [fitness_fn(x) for x in population]

    # Handle case where all fitness values are negative
    min_fitness = min(fitness_values)
    if min_fitness < 0:
        # Shift all values to be non-negative
        adjusted_fitness = [f - min_fitness + 1 for f in fitness_values]
    else:
        adjusted_fitness = fitness_values

    total_fitness = sum(adjusted_fitness)

    # If total fitness is 0, select randomly
    if total_fitness == 0:
        return random.sample(list(population), 2)

    # Roulette wheel selection
    selected = []
    for _ in range(2):
        pick = random.uniform(0, total_fitness)
        current = 0
        for i, individual in enumerate(population):
            current += adjusted_fitness[i]
            if current >= pick:
                selected.append(individual)
                break

    # If somehow we didn't select 2 (edge case), pick randomly
    while len(selected) < 2:
        selected.append(random.choice(list(population)))

    return selected[0], selected[1]

def get_initial_queens_population(n_queens, count):
    """Generate initial population for n-queens problem"""
    population = set()
    while len(population) < count:
        # Create a random permutation of rows (0 to n_queens-1)
        individual = tuple(random.sample(range(n_queens), n_queens))
        population.add(individual)
    return population

def main():
    start = time.time()
    print("Starting n-queens genetic algorithm...")
    n_queens = 8
    population_size = 20  # Larger population for n-queens

    # Generate initial population
    initial_population = get_initial_queens_population(n_queens, population_size)

    # Use the positive fitness function (maximize non-conflicting pairs)
    fittest = genetic_algorithm(initial_population, queens_fitness.fitness_fn_positive, n_queens)

    print('Solution found: ' + str(fittest))
    print('Fitness: ' + str(queens_fitness.fitness_fn_positive(fittest)))
    print('Conflicts: ' + str(queens_fitness.fitness_fn_negative(fittest)))
    end = time.time()
    print('Time taken: ' + str(math.floor(end - start)) + ' seconds')
    # Display the board (optional)
    display_board(fittest)

def display_board(solution):
    """Display the chessboard with queens"""
    n = len(solution)
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)

if __name__ == '__main__':
    main()
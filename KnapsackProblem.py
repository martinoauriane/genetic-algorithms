import random

CHROMOSOME_LEN = 10
POPULATION_LENGTH = 10
GENERATIONS = 10

obj = [ [2, 6], [3, 5], [6, 8], [7, 9], [5, 6], [9, 7], [4, 6], [1, 3],  [8, 10], [6, 7] ]
#[0, 1, 1, 0, 1, 0, 1, 0, 0, 0]


def generate_gene(): 
    return random.randint(0, 1)

def generate_chromosom():
    final_chromosome = []
    for i in range(CHROMOSOME_LEN):
        gene = generate_gene()
        final_chromosome.append(gene)
    return final_chromosome

def generate_population():
    population = []
    for i in range(POPULATION_LENGTH):
        chromosome = generate_chromosom()
        population.append(chromosome)
    return population 

def fitness(final_chromosome, obj):
    valeur = 0
    poids = 0
    for (gene, obj_entries) in zip(final_chromosome, obj):
        if gene == 1: 
            valeur += obj_entries[1]
            poids += obj_entries[0]
        
    if poids > 20: 
        return 0
    else :
        return valeur 

def croisement(survivors):
    parent1 = random.choice(survivors)
    parent2 = random.choice(survivors)
    while parent1 == parent2:
        parent2 = random.choice(survivors)
    point = random.randint(1, CHROMOSOME_LEN - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def make_children(survivors):
    children = []
    while len(children) < 5:
        child1, child2 = croisement(survivors)
        children.append(child1)
        if(len(children) == 5):
            break
        children.append(child2)
    return children

def mutation(population, mutation_rate=0.5):
    for chromosome in population: 
        for i in range(CHROMOSOME_LEN):
            if random.random() < mutation_rate:
                chromosome[i] = 1 - chromosome[i]
    return population

def genetic_algorithm():
    population = generate_population()
    
    for i in range(0, GENERATIONS):
        fitness_scores = []
        for i in range(POPULATION_LENGTH):
            score = fitness(population[i], obj)
            fitness_scores.append(score) # fitness
        #selection
        population_with_fitness = list(zip(population, fitness_scores))
        population_with_fitness.sort(key=lambda x: x[1], reverse=True)

        survivors = [individual[0] for individual in population_with_fitness[:5]]

        # croisement
        children = make_children(survivors)
        population = survivors + children

        # mutation 
        population = mutation(population)
        
        print(f"Generation {i}: population = {population}\n", i, population)
        print("\n")

genetic_algorithm()

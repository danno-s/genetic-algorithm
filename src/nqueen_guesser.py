import random
from nqueen_individual import NQueenIndividual
import filtering
from population import Population
from time import time
from sys import argv
from statistics import mean, stdev

POPULATION_SIZE = 100

if __name__ == "__main__":
    n = int(input("Ingrese número de reinas: "))

    if n == 2 or n == 3:
        raise Exception("No existen soluciones para ese número de reinas")
    
    # Definimos las funciones necesarias para el algoritmo genético
    def attacks(queen, anotherQueen):
        # Horizontal
        if queen[0] == anotherQueen[0]:
            return True
        # Vertical
        if queen[1] == anotherQueen[1]:
            return True
        # Diagonal
        if abs(queen[0] - anotherQueen[0]) == abs(queen[1] - anotherQueen[1]):
            return True
        return False
    
    def fitness(an_individual):
        collisions = 0
        for queen in an_individual.queens:
            for otherQueen in an_individual.queens:
                if queen != otherQueen:
                    # Revisar si se atacan
                    if attacks(queen, otherQueen):
                        collisions += 1
        
        return -collisions

    population = Population(POPULATION_SIZE, lambda: NQueenIndividual(n), fitness, filtering.fittest_quarter)

    generations = 1
    gen_fitness = []
    gen_change = []
    solution = None

    if len(argv) == 2:
        log = open(argv[1], 'w')
        log.write("Generación,Fitness,Máximo\n")

    start = time()
    while True:
        population.compute_fitness()

        # Conseguimos el elemento de mejor fitness
        sorted_individuals = sorted(population.individual_fitness.items(), key=lambda kv: kv[1])

        # Si el fitness es el número de bits de la frase
        if sorted_individuals[-1][1] == 0:
            # La solución es el par asociado a ese fitness
            solution = sorted_individuals[-1][0]

        print("\033[KBest individual fitness: {}".format(sorted_individuals[-1][1]), end="\r")
        if len(gen_fitness) == 0 or gen_fitness[-1] != sorted_individuals[-1][1]:
            gen_fitness.append(sorted_individuals[-1][1])
            gen_change.append(generations)

        if len(argv) == 2:
            # Logeamos las estadísticas de esta generación
            for _, f in sorted_individuals:
                log.write("{},{},{}\n".format(generations, f, gen_fitness[-1]))

        if solution:
            break

        generations += 1
        population.filter_population()
        population.reproduce()

    if len(argv) == 2:
        log.close()
    end = time()
    print("\033[KSolución encontrada en {} generaci{}. Tiempo total: {} segundos".format(generations, "ón" if generations == 1 else "ones", end - start))
    print("Fitness máxima de cada generación: " + " ".join("\n\tGen " + str(gen) + ": " +  str(fitness) for gen, fitness in zip(gen_change, gen_fitness)))
    print("Respuesta encontrada: {}".format(solution.queens))

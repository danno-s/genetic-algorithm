import random
from bit_individual import BitIndividual
from filtering import probabilistic_filter
from population import Population

if __name__ == "__main__":
    target_bits = input("Ingrese bits para adivinar: ")
    if target_bits.replace("1", "").replace("0", "") != "":
        raise Exception("bits ingresados no válidos")

    n_bits = len(target_bits)
    
    # Definimos las funciones necesarias para el algoritmo genético
    def individual_generator():
        return BitIndividual(n_bits)

    def fitness(an_individual):
        fitness = 0
        for target, actual in zip(target_bits, an_individual.bits):
            if target == actual:
                fitness += 1
        return fitness

    population = Population(100, individual_generator, fitness, probabilistic_filter([0, n_bits]))

    generations = 1
    max_fitness = []
    solution = None

    while True:
        population.compute_fitness()

        # Conseguimos el elemento de mejor fitness
        sorted_individuals = sorted(population.individual_fitness.items(), key=lambda kv: kv[1])

        # Si el fitness es el número de bits de la frase
        if sorted_individuals[-1][1] == n_bits:
            # La solución es el par asociado a ese fitness
            solution = sorted_individuals[-1][0]


        print("\033[KBest individual fitness: {}".format(sorted_individuals[-1][1]), end="\r")
        max_fitness.append(sorted_individuals[-1][1])

        if solution:
            break

        generations += 1
        population.filter_population()
        population.reproduce()


    print("\033[KSolución encontrada en {} generaci{}.".format(generations, "ón" if generations == 1 else "ones"))
    print("Fitness máxima de cada generación: " + " ".join("\n\tGen " + str(i + 1) + ": " +  str(max_fitness[i]) for i in range(generations)))
    print("Respuesta encontrada: {}".format(solution.bits))
import random
from bit_individual import BitIndividual
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

    def filter_population(self):
        to_remove = []
        for individual, fitness in self.individual_fitness.items():
            if random.random() > fitness / n_bits:
                to_remove.append(individual)
        for individual in to_remove:
            self.individual_fitness.pop(individual)

    population = Population(100, individual_generator, fitness, filter_population)

    solution = None

    while True:
        population.compute_fitness()

        # Conseguimos el elemento de mejor fitness
        sorted_individuals = sorted(population.individual_fitness.items(), key=lambda kv: kv[1])

        if sorted_individuals[-1] == n_bits:
            solution = sorted_individuals[-1][0]
            break

        population.filter_population()
        population.reproduce()

    print("Bits encontrados: {}".format(solution.bits))
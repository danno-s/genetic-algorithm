import random

mutation_rate = 0.05

class BitIndividual:
    def __init__(self, n_bits):
        '''Crea un nuevo individuo con un número binario al azar
        '''
        self.n_bits = n_bits
        self.bits = bin(random.getrandbits(n_bits))[2:]
        if len(self.bits) < n_bits:
            self.bits = "0" * (n_bits - len(self.bits)) + self.bits

    def reproduce(self, another_bit_individual):
        '''Crea un nuevo individuo, a base de este y otro individuo, 
        con mutaciones al azar
        '''
        child = BitIndividual(self.n_bits)

        division = random.randint(0, self.n_bits)
        child.bits = self.bits[:division] + another_bit_individual.bits[division:]

        mutated_bits = ""

        for i in range(self.n_bits):
            if random.random() < mutation_rate:
                mutated_bits += "0" if child.bits[i] == "1" else "1"
            else:
                mutated_bits += child.bits[i]

        child.bits = mutated_bits

        return child

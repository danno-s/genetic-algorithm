from random import randint, random

mutation_rate = 0.2

'''Clase que representa una solución al problema de N reinas en un tablero de NxN.
La solución se representa simplemente con las posiciones de las N reinas.
'''
class NQueenIndividual:
    def __init__(self, n):
        '''Crea un intento de solución para el problema de N reinas en un tablero NxN
        '''
        self.n = n
        self.queens = []
        for _ in range(n):
            while True:
                new_queen = [randint(0, n - 1), randint(0, n - 1)]
                if new_queen not in self.queens:
                    self.queens.append(new_queen)
                    break


    def reproduce(self, another_nqueens):
        '''Crea una nueva solución, a partir de las dos soluciones padres
        '''
        child = NQueenIndividual(self.n)

        division = randint(0, self.n)
        child.queens = self.queens[:division]

        for new_queen in another_nqueens.queens[division:]:
            if new_queen in child.queens:
                while True:
                    new_queen = [randint(0, self.n - 1), randint(0, self.n - 1)]
                    if new_queen not in child.queens:
                        break
            child.queens.append(new_queen)

        for i in range(self.n):
            # Si se muta, poner una reina completamente nueva
            if random() < mutation_rate:
                while True:
                    new_queen = [randint(0, self.n - 1), randint(0, self.n - 1)]
                    if new_queen not in child.queens:
                        child.queens[i] = new_queen
                        break

        return child

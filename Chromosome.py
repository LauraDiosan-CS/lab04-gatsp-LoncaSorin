from random import randint, random
from utils import generatePermutation

class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam
        self.__fitness = 0.0
        self.__repres = []
    
    @property
    def repres(self):
        return self.__repres
    
    @property
    def fitness(self):
        return self.__fitness 
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit = 0.0):
        self.__fitness = fit 

    def initialization(self, lungime, matrice):
        #generam random genele din comunitate
        self.__repres = generatePermutation(0, self.__problParam['noDim'])
    
    def crossover(self, c):
        pos1 = randint(-1, self.__problParam['noNodes'] - 1)
        pos2 = randint(-1, self.__problParam['noNodes'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1 
        k = 0
        newrepres = self.__repres[pos1 : pos2]
        for el in c.__repres[pos2:] +c.__repres[:pos2]:
            if (el not in newrepres):
                if (len(newrepres) < self.__problParam['noNodes'] - pos1):
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1

        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        return offspring
    
    def _rand_subpath(self):
        i = j = randint(-1, self.__problParam['noNodes'] - 1)

        while i == j:
            j = randint(-1, self.__problParam['noNodes'] - 1)

        return min(i, j), max(i, j)

    def _crossover_ox(self, c):

        # Initial child path
        child = Chromosome(self.__problParam)

        # Copy random subpath from parent 1 to child
        start, end = self._rand_subpath()
        subpath = self.__repres[start:end+1]
        tmp = c.__repres

        # Rotate tmp with pivot in the end + 1
        tmp = tmp[end+1:] + tmp[:end+1]
        # Remove cities found in subpath from parent 2
        tmp = list(filter(lambda x: x not in subpath, tmp))

        # Join subpath and tmp to form a child
        child.__repres = subpath + tmp

        # Rotate the path so it always starts at 0
        last_zero_idx = len(child.__repres) - child.__repres[::-1].index(0) - 1
        child.__repres = child.__repres[last_zero_idx:] + child.__repres[:last_zero_idx]

        return child
    
    def mutation(self):
        pos1 = randint(-1, self.__problParam['noNodes'] - 1)
        pos2 = randint(-1, self.__problParam['noNodes'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)
        
    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
    
    def __lt__(self, c):
        return self.__fitness < c.__fitness
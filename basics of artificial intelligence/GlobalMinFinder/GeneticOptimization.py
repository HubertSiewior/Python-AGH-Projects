import numpy as np


class Genetic(object):

    def __init__(self, f, pop_size=5, n_variables=2):
        self.f = f
        self.minim = -100
        self.maxim = 100
        self.pop_size = pop_size
        self.n_variables = n_variables
        self.population = self.initializePopulation()
        self.evaluatePopulation()

    def initializePopulation(self):
        return [np.random.randint(self.minim, self.maxim, size=self.n_variables)
                for i in range(self.pop_size)]

    def showGeneration(self):
        target = np.random.randint(0, 1, size=self.n_variables)
        fitness = 0
        fitnessList = []
        i = 0

        for chrom in self.population:
            fitness = 0
            if chrom[0] == target[0]:
                fitness += 1
            if chrom[1] == target[1]:
                fitness += 1
            i += 1
            fitnessList.append(fitness)

        for i in range(len(self.population)):
            print('Chromosome # ', i, '\tFitness: ', fitnessList[i], '\t', self.population[i])

    def evaluatePopulation(self):
        return [self.f(i[0], i[1]) for i in self.population]

    def nextGeneration(self):
        results = self.evaluatePopulation()
        children = [self.population[np.argmin(results)]]

        while len(children) < self.pop_size:
            # Tournament selection
            randA = np.random.randint(0, self.pop_size)
            randB = np.random.randint(0, self.pop_size)
            if results[randA] < results[randB]:
                p1 = self.population[randA]

            else:
                p1 = self.population[randB]

            randA = np.random.randint(0, self.pop_size)
            randB = np.random.randint(0, self.pop_size)
            if results[randA] < results[randB]:
                p2 = self.population[randA]
            else:
                p2 = self.population[randB]

            signs = []
            for i in zip(p1, p2):
                if i[0] < 0 and i[1] < 0:
                    signs.append(-1)
                elif i[0] >= 0 and i[1] >= 0:
                    signs.append(1)
                else:
                    signs.append(np.random.choice([-1, 1]))

            # Converting to binary
            p1 = [format(abs(i), '010b') for i in p1]
            p2 = [format(abs(i), '010b') for i in p2]

            # Recombination and mutation
            mutation_probability = 10
            child = []
            for i, j in zip(p1, p2):
                for k, l in zip(i, j):
                    if k == l:
                        if np.random.randint(0, 100) <= mutation_probability:
                            k = 1 - int(k)
                            child.append(str(k))
                        else:
                            child.append(str(k))
                    else:
                        if np.random.randint(0, 100) <= mutation_probability:
                            child.append(str(np.random.randint(min(int(k) + 1, int(l) + 1),
                                                               max(int(k) + 1, int(l) + 1))))
                        else:
                            child.append(str(np.random.randint(min(k, l),
                                                               max(k, l))))

            child = ''.join(child)
            g1 = child[0:len(child) // 2]
            g2 = child[len(child) // 2:len(child)]
            children.append(np.asarray([signs[0] * int(g1, 2),
                                        signs[1] * int(g2, 2)]))

        self.population = children

    def run(self):
        ix = 0

        target = np.random.randint(0, 1, size=self.n_variables)

        print('Generation 0')
        self.showGeneration()

        war = True
        index2 = 0
        while True:
            ix += 1
            self.nextGeneration()
            print('\nGeneration ', ix)
            self.showGeneration()

            index = 0
            for chrom in self.population:
                fitness = 0
                if chrom[0] == target[0]:
                    fitness += 1
                if chrom[1] == target[1]:
                    fitness += 1
                if fitness == 2:
                    war = False
                    index2 = index
                index += 1

            if not war:
                break
        return self.population[index2]


print('Target: [0, 0]')
function = lambda x, y: 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y
gen = Genetic(function)
minim = gen.run()
print('Minimum found       X =', minim[0], ', Y =', minim[1])

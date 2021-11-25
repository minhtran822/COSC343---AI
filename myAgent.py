import numpy as np
import math
from numpy.random import seed
from copy import deepcopy

#COSC343 Assignment 2: Evolving a species
#Minh Tran - 6355049

playerName = "myAgent"
nPercepts = 75  #This is the number of percepts
nActions = 7    #This is the number of actionss
seed(1)
s=7            #sample size
elitism = 15
# This is the class for your creature/agent

class MyCreature:

    def __init__(self):
        # You should initialise self.chromosome member variable here (whatever you choose it
        # to be - a list/vector/matrix of numbers - and initialise it with some random
        # values
        self.chromosome = np.random.random((nPercepts, nActions))
        
        pass #This is just a no-operation statement - replace it with your code


    def AgentFunction(self, percepts):

        actions = np.zeros((nActions))

        # You should implement a model here that translates from 'percepts' to 'actions'
        # through 'self.chromosome'.
        #

        input = percepts.ravel()
        # The 'actions' variable must be returned and it must be a 7-dim numpy vector or a
        # list with 7 numbers.
        #
        # The index of the largest numbers in the 'actions' vector/list is the action taken
        # with the following interpretation:
        # 0 - move left
        # 1 - move up
        # 2 - move right
        # 3 - move down
        # 4 - do nothing
        # 5 - eat
        # 6 - move in a random direction
        #
        # Different 'percepts' values should lead to different 'actions'.  This way the agent
        # reacts differently to different situations.
        #
        # Different 'self.chromosome' should lead to different 'actions'.  This way different
        # agents can exhibit different behaviour.

        #Using matrix multiplication, we assign weight to the corresponding percept tile and related action
        actions = input @ self.chromosome

        return actions

def newGeneration(old_population):

    # This function should return a list of 'new_agents' that is of the same length as the
    # list of 'old_agents'.  That is, if previous game was played with N agents, the next game
    # should be played with N agents again.

    # This function should also return average fitness of the old_population
    N = len(old_population)

    # Fitness for all agents
    fitness = np.zeros((N))
    death = 0

    # This loop iterates over your agents in the old population - the purpose of this boiler plate
    # code is to demonstrate how to fetch information from the old_population in order
    # to score fitness of each agent
    for n, creature in enumerate(old_population):

        # creature is an instance of MyCreature that you implemented above, therefore you can access any attributes
        # (such as `self.chromosome').  Additionally, the objects has attributes provided by the
        # game enginne:
        #
        # creature.alive - boolean, true if creature is alive at the end of the game
        # creature.turn - turn that the creature lived to (last turn if creature survived the entire game)
        # creature.size - size of the creature
        # creature.strawb_eats - how many strawberries the creature ate
        # creature.enemy_eats - how much energy creature gained from eating enemies

        # This fitness functions considers length of survival, alive state, size, number of strawberry
        # and energy gained, with the weight on the size, energy gained from enemies and state of alive
        fitness[n] = (creature.alive + creature.turn/90) * (creature.turn) * ((creature.strawb_eats) ** (creature.size+1)) * (creature.enemy_eats)
        death += creature.turn

    # At this point you should sort the agent according to fitness and create new population
    new_population = list()
    for n in range(N):

        # Create new creature
        new_creature = MyCreature()

        # Here you should modify the new_creature's chromosome by selecting two parents (based on their
        # fitness) and crossing their chromosome to overwrite new_creature.chromosome

        # Consider implementing elitism, mutation and various other
        # strategies for producing new creature.

        subset = np.random.choice(N, s, replace=False)
        largest = 0
        second = 0
        subsum = fitness[subset[0]]

        #Elitism is obtained through comparing to the maximum fitness score
        #The elitism range is applied to keep close to the data
        global elitism
        if(np.max(fitness) > 16):
            if(np.max(fitness) > (elitism*1.5) or elitism > (np.max(fitness)*1.5)):
                elitism = np.max(fitness) - 1

        #Tournament selection is applied to find the best two parents
        for i in range(1,s):
            subsum += fitness[subset[i]]
            if (fitness[subset[i]] >= fitness[subset[largest]]):
                largest = i
            # if (fitness[subset[i]] >= fitness[subset[largest]]):
            #     second=largest
            #     largest = i
            # elif(fitness[subset[i]] < fitness[subset[largest]] and fitness[subset[i]] >= fitness[subset[second]]):
            #     second=i

        subfitness = np.random.random(1)
        for i in range (0,s):
            subfitness -= (fitness[subset[i]]/subsum)
            if(subfitness <0):
                second = i
            elif(i == s-1 and subfitness > 0):
                second = np.random.randint(len(subset))
                print("ERRORRRRRRRRRRRRRRR")

        #second = np.random.randint(len(subset))

        parent1=deepcopy(old_population[subset[largest]].chromosome)
        parent2=deepcopy(old_population[subset[second]].chromosome)

        new_creature.chromosome = deepcopy(parent1)

        r=np.random.random(1)

        #crossover of chromosome using uniform crossover. This step is ignored if the parent is in elitism
        if (fitness[subset[largest]] < elitism):
            for i in range(nActions):
                for j in range(nPercepts):

                    # if(j % 25 ==0):
                    #     r=np.random.random(1)

                    if(r > 0.5):
                        if(j <25):
                            new_creature.chromosome[j][i] = parent1[j][i]
                        elif(j<50):
                            new_creature.chromosome[j][i] = parent2[j][i]
                        else:
                            new_creature.chromosome[j][i] = parent1[j][i]
                    else:
                        if(j <25):
                            new_creature.chromosome[j][i] = parent2[j][i]
                        elif(j<50):
                            new_creature.chromosome[j][i] = parent1[j][i]
                        else:
                            new_creature.chromosome[j][i] = parent2[j][i]

                            
                    mutation = np.random.random(1)

                    if(mutation < 0.002): # 5/(75*34)
                        new_creature.chromosome[j][i] = np.random.random(1)
                    
                    # if(j <25):
                    #     new_creature.chromosome[j][i] = parent1[j][i] #retain the eating process
                    # else:
                    #     r=np.random.random(1)
                    #     if(r > 0.5):
                    #         new_creature.chromosome[j][i] = parent1[j][i]
                    #     else:
                    #         new_creature.chromosome[j][i] = parent2[j][i]


        # Add the new agent to the new population
        new_population.append(new_creature)

    # At the end you need to compute average fitness and return it along with your new population
    avg_fitness = np.mean(fitness)

    return (new_population, avg_fitness)

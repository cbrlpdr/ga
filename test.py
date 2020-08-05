from pyeasyga import pyeasyga
import random

data = [("A",20), ("B",50), ("C",75), ("D",25), ("E",25), ("F",78)]

ga = pyeasyga.GeneticAlgorithm(data,8,100,0.9,0.8,True,True)

def create_individual(data):
    return [random.randint(-1, 1) for _ in range(len(data))]

ga.create_individual = create_individual
def fitness(individual, data):
    fn = 0
    auxCounter=0
    goal=125
    sm=0

    for (selected, (_, profit)) in zip(individual, data):
        if selected==1:
            sm += profit
        elif selected==-1:
            sm -= profit
            #auxCounter +=1
    fn = 1/(abs(goal-sm)+0.01)
    #fn -= auxCounter*2 
    return fn
            
ga.fitness_function = fitness

ga.run()

#for individual in ga.last_generation():
    #print (individual)

print (ga.best_individual())
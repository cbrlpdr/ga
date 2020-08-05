from pyeasyga import pyeasyga
import random
import itertools

#data = [("A",20), ("B",50), ("C",75), ("D",25), ("E",25), ("F",78)]
data = [("A",25),("B",42),("C",37),("D",40),("E",27),("F",43),("G",36),("H",-123),("I",-210)]
ga = pyeasyga.GeneticAlgorithm(data,8,100,0.9,0.8,True,True)

def create_individual(data):
    numClusters=3
    return [random.randint(0,numClusters-1) for _ in range(len(data))]

ga.create_individual = create_individual
def fitness(individual, data):
    fn = 0
    numClusters=3
    lstSomatorios = []
    for i in range(numClusters):
        lsProfit=[]
        for (selected, (_, profit)) in zip(individual, data):
            if(selected == i): lsProfit.append(profit)
        
        sm=0
        for a in itertools.combinations(lsProfit,2):
            for i in range(len(a)-1):
                sm+=abs(a[i]-a[i+1]) 
        lstSomatorios.append(sm*len(lsProfit))

    for p in lstSomatorios:
        fn+= p 
    
    fn = numClusters/fn
    return fn
            
ga.fitness_function = fitness

ga.run()

#for individual in ga.last_generation():
    #print (individual)

print (ga.best_individual())
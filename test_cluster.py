from pyeasyga import pyeasyga as galg
import random
import itertools
import matplotlib.pyplot as plt
import numpy as np

#data = [("A",20), ("B",50), ("C",75), ("D",25), ("E",25), ("F",78)]
data = [("A",5,5),("B",3,10),("C",5,12),("D",16,2),("E",15,9),("F",21,21),("G",22,20)]
ga = galg.GeneticAlgorithm(data,20,500,0.8,0.4,True,True)

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
        for (selected, (_, x,y)) in zip(individual, data):
            if(selected == i): lsProfit.append((x,y))
        
        sm=0
        for a in itertools.combinations(lsProfit,2):
            A = a[0]
            B = a[1]
            sm+=pow(abs(pow(A[0]-B[0],2)+pow(A[1]-B[1],2)),0.5)
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
bestind=ga.best_individual()
cromossome=bestind[1]

colorset=["#f00","#0f0","#00f","#0ff"]
fig, ax = plt.subplots()
numClusters=3
for clusterInd in range(numClusters):
    i=0
    for pt in data:
        if(clusterInd==cromossome[i]):
            ax.plot(pt[1],pt[2],"*",c=colorset[clusterInd])
            ax.text(pt[1]-0.15,pt[2]+0.4,data[i][0])
        i+=1

plt.show()

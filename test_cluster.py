from pyeasyga import pyeasyga as galg
import random
import itertools
import matplotlib.pyplot as plt
import numpy as np

global pmVec
pmVec=[(0,0),(0,0),(0,0)]

data = [("A",5,5),("B",3,10),("C",5,12),("D",16,2),("E",15,9),("F",21,21),("G",22,20)]
ga = galg.GeneticAlgorithm(data,20,1000,1,0.4,True,True)

def create_individual(data):
    numClusters=3
    return [random.randint(0,numClusters-1) for _ in range(len(data))]

ga.create_individual = create_individual
def fitness(individual, data):
    fn = 0
    numClusters=3
    for i in range(numClusters):
        #Pra cada cluster cria uma lista de elementos pertencentes apenas a ela
        lsElements=[]
        clusterEmpty=True
        for (selected, (_, x,y)) in zip(individual, data):
            if(selected == i): 
                lsElements.append((x,y))
                clusterEmpty=False #Checa se existe alguma cluster vazia
        if(clusterEmpty):
            return 0 #Caso a cluster analisada esteja vazia retorna fitness 0
        
        if(len(lsElements)==0): break
        smCluster=0
        pmX=0
        pmY=0
        clusterSize=len(lsElements)
        #Define o ponto médio entre os elementos da cluster
        for (x,y) in lsElements:
            pmX+=x
            pmY+=y
        pmX/=clusterSize
        pmY/=clusterSize
        pmVec[i]=(pmX,pmY)
        #Calcula a soma das distâncias dos pontos da cluster até o centro dela
        for (x,y) in lsElements:
            smCluster+=pow(pow(x-pmX,2)+pow(y-pmY,2),0.5)
        #Calcula a média das distâncias (evita que clusters que tenham muitos elementos acabem com uma fitness reduzida indevidamente)
        smCluster*=clusterSize
        fn+=smCluster
    fn=numClusters/fn

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
for (pmx,pmy) in pmVec:
    ax.plot(pmx,pmy,".")

plt.show()

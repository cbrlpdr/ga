from pyeasyga import pyeasyga as galg
import random
import itertools
import matplotlib.pyplot as plt
import numpy as np

global pmVec
global numClusters
numClusters=3
dataSize=100
data=[]
roof=1000
for a in range(dataSize):
    data.append(("",random.randint(0,roof),random.randint(0,roof)))

popSize=20
numGenerations=500
crossoverProb=0.4
mutationProb=0.8

ga = galg.GeneticAlgorithm(data,popSize,numGenerations,crossoverProb,mutationProb,True,True)

def create_individual(data):
    return [random.randint(0,numClusters-1) for _ in range(len(data))]

def mutate(individual):
    mutate_index = random.randrange(len(individual))
    individual[mutate_index]=random.randint(0,numClusters-1)
ga.mutate_function = mutate
ga.create_individual = create_individual
def fitness(individual, data):
    fn = 0
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

colorset=["#f00","#0f0","#00f","#0cf","#ff0","#2b2","#0aa","#aac"]
fig, ax = plt.subplots()
pmx = 0 
pmy = 0
for clusterInd in range(numClusters):
    i=0
    for pt in data:
        if(clusterInd==cromossome[i]):
            ax.plot(pt[1],pt[2],".",c=colorset[clusterInd])
            ax.text(pt[1]-0.15,pt[2]+0.4,data[i][0])
        i+=1


plt.show()

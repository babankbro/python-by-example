import math
import random
from ga01 import *


def generation(chs, PC, PM):
    N = len(chs)
    NG = len(chs[0])
    fitList = createRouletteWheel(chs)
    accuList = cumulative(fitList)
    nextChs = []
    for i in range(0, N, 2):
        p1 = chs[selection(accuList, random.random()*100)]
        p2 = chs[selection(accuList, random.random()*100)]
        c1 = p1[:]
        c2 = p2[:]
        if random.random() < PC:
            c1, c2 = crossover(p1, p2, random.randint(0, NG-1))
        
        if random.random() < PM:
            mutate(c1, random.randint(0, NG-1))
        if random.random() < PM:
            mutate(c2, random.randint(0, NG-1))
        nextChs.append(c1)
        nextChs.append(c2)
    return nextChs

def findBest(chs):
    fitList = calulateFitnessAll(chs)
    maxVal = fitList[0]
    maxi = 0
    for i in range(1, len(fitList)):
        if maxVal < fitList[i]:
            maxValue = fitList[i]
            maxi = i
    return maxi, fitList

def ga():
    N = 10
    NG = 7
    PC = 0.7
    PM = 0.3
    random.seed(3)
    chs = intial(N, NG)
    
    besti, fitList = findBest(chs)
    bestValue = fitList[besti]
    best = chs[besti][:]

    for i in range(100):
        chs = generation(chs, PC, PM)
        besti, fitList = findBest(chs)
        if fitList[besti] > bestValue:
            best = chs[besti][:]
            bestValue = fitList[besti]

        print(i, bestValue)

    printChros(chs)
    print()
    x = decode(best)
    print(x ,(best),  fitness(x))    
    

ga()
    












    










import math
import random

def printChros(cs):
    i = 1
    fitList = createRouletteWheel(cs)
    accuList = cumulative(fitList)
    print("Chros" +"\t"+ "Value"
              +"\t"+ "Genes"+"\t\t\t"+ "Fitness" + "\t" +"Percent" +
          "\t" +"Accu")
    for c in cs:
        x = decode(c)
        f = round(fitness(x), 2)
        print("X"+str(i) +"\t"+ str(x)
              +"\t"+ str(c)+"\t"+ str(f) + "\t" +str(fitList[i-1])+
              "\t" +str(accuList[i-1]))
        i += 1

def fitness(x):
    a = 35
    b = 1.22
    c = 2
    return a*math.exp( -(x-b)*(x-b)/(2*c*c))

def f(x):
    return 6-3*x +x*x

aa = 1
bb = 2
def rangeX(dx, mx, a, b):
    return (dx/mx)*(b-a)+a

def decode(c):
    global aa, bb
    x = 0
    N = len(c)
    for i in range(N):
        b = c[N - 1 - i]
        x += b*(2**i)
    return  rangeX(x, 2**N-1, aa, bb)
    #return x

c1 = [0, 0, 0 , 1, 0, 1, 1]

print( decode(c1))



def createRandom(Ng):
    c = []
    for i in range(Ng):
        c.append(random.choice([0, 1]))
    return c


def intial(N, Ng):
    listChro = []
    for i in range(N):
        c = createRandom(Ng)
        listChro.append(c)
    return listChro

def calulateFitnessAll(cs):
    fitList = []
    for c in cs:
        x = decode(c)
        f = round(fitness(x), 2)
        fitList.append(f)
    return fitList

def createRouletteWheel(cs):
    sumf = 0
    fitList = calulateFitnessAll(cs)
    for f in fitList:
        sumf += f
    #print("Sumf", sumf)
    for i in range( len(fitList)):
        fitList[i] = round(fitList[i]/sumf*100, 2)

    return fitList

def cumulative(fitList):
    accuList = [fitList[0]]
    for i in range( 1, len(fitList)):
        accuList.append(accuList[i-1] + fitList[i])
    return accuList

def selection(accuList, percent):
    for i in range(len(accuList)):
        if percent < accuList[i]:
            return i
    return len(accuList)-1

def crossover(p1, p2, posCut):
    c1 = []
    c2 = []
    for i in range(posCut):
        c1.append(p1[i])
        c2.append(p2[i])

    for i in range(posCut, len(p1)):
        c1.append(p2[i])
        c2.append(p1[i])
    return c1, c2

def mutate(c, pos):
    if c[pos] == 1:
        c[pos] = 0
    else:
        c[pos] = 1

def testMethods():
    global aa, bb
    random.seed(3)
    chromosomes = intial(4, 7)
    aa = 0
    bb = 2**7 - 1
    printChros(chromosomes)

    
    fitList = createRouletteWheel(chromosomes)
    accuList = cumulative(fitList)
    print(accuList)
    print("Selection 55", "X"+str(selection(accuList, 55)+1))
    print("Selection 10", "X"+str(selection(accuList, 10)+1))

    p1 = chromosomes[selection(accuList, 55)]
    p2 = chromosomes[selection(accuList, 10)]

    print("=========== Crossover ===========")
    print("P1", p1)
    print("P2", p2)
    c1, c2 = crossover(p1, p2, 3)
    print("---------------------------------")
    print("C1", c1)
    print("C2", c2)
    print()

    print("=========== Mutation ===========")
    print("Before", c1, decode(c1))
    mutate(c1, 4)
    print("---------------------------------")
    print("After ", c1, decode(c1))

testMethods()

    












    










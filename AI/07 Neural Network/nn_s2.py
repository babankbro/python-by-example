import random

def f(x):
    if x > 0:
        return 1
    else:
        return 0

def sumX(w1, w2, x1, x2, th):
    return w1*x1 + w2*x2 + th

def delta(a, x, e):
    return a*x*e

random.seed(0)
print("================= Pharse 2")
w1 = random.random()
w2 = random.random()
th = -random.random()
x1s = [0, 0, 1, 1]
x2s = [0, 1, 0, 1]
yds = [0, 1, 1, 0]
a = 0.1 #

print("X1\tX2\tYd\tY\tError\tW1\tW2\tTh")

while True:

    sumE = 0
    
    for i in range(len(yds)):
        x1 = x1s[i]
        x2 = x2s[i]
        yd = yds[i]
        
        sx = sumX(w1, w2, x1, x2, th)
        y = f(sx)

        e = yd - y
        dw1 = delta(a, x1, e)
        dw2 = delta(a, x2, e)
        dth = delta(a, 1, e)
        w1 = w1 + dw1
        w2 = w2 + dw2
        th = th + dth

        output = str(round(x1,2))+"\t" + str(round(x2,2))+"\t"+ str(round(yd,2))+"\t" +\
             str(round(y,2))+"\t" + str(round(e,2))+"\t" +str(round(w1,2))+"\t" +\
             str(round(w2,2))+"\t" + str(round(th,2))
        print(output)

        sumE += e*e

    print('------------------------------------------------------')
    
    if sumE == 0:
        break



x1 = 1
x2 = 0
sx = sumX(w1, w2, x1, x2, th)
y = f(sx)
print("Y =", y)













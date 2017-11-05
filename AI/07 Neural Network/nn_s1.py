def f(x):
    if x > 0:
        return 1
    else:
        return 0


def sumX(w1, w2, x1, x2, th):
    return w1*x1 + w2*x2 + th


def delta(a, x, e):
    return a*x*e


w1 = 0.3
w2 = 0.2
th = -0.2

x1 = 0
x2 = 1
yd = 1

a = 0.1

print("Data w1, w2, th, x1, x2 =", w1, w2, th, x1, x2)
sx = sumX(w1, w2, x1, x2, th)
print("Sx =", sx)

y = f(sx)
print("y =", y)

e = yd - y
print("e =", e)

dw1 = delta(a, x1, e)
dw2 = delta(a, x2, e)
dth = delta(a, 1, e)
print("dw1 =", dw1)
print("dw2 =", dw2)
print("dth =", dth)

w1 = w1 + dw1
w2 = w2 + dw2
th = th + dth
print("Data w1, w2, th, x1, x2 =", w1, round(w2, 2), th, x1, x2)
import random
print()
print("================= Pharse 2")
w1 = random.random()
w2 = random.random()
th = -random.random()
x1 = 0
x2 = 1
yd = 1
a = 0.01 #

print("X1\tX2\tYd\tY\tError\tW1\tW2\tTh")
output = str(round(x1,2))+"\t" + str(round(x2,2))+"\t"+ str(round(yd,2))+"\t" +\
         "-\t-\t" +str(round(w1,2))+"\t" +\
         str(round(w2,2))+"\t" + str(round(th,2))
print(output)

while True:

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
    
    if e == 0:
        break



















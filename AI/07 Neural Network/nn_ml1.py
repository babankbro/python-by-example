import math

def f(x):
    print("ex", math.exp(-x))
    print("1 + ex", 1  + math.exp(-x))
    return 1/(1+math.exp(-x))

def sumX(w1, w2, x1, x2, th):
    return w1*x1 + w2*x2 - th


x1 = 1
x2 = 1

w13 = 0.5
w23 = 0.4
th3 = 0.8

w14 = 0.9
w24 = 1.0
th4 = -0.1

w35 = -1.2
w45 = 1.1
th5 = 0.3

yd5 = 0
a = 0.2 

s3 = sumX(w13, w23, x1, x2, th3)
y3 = f(s3)

print("Sx3 =",s3)
print("y3 =", round(y3,4)) 
print()

s4 = sumX(w14, w24, x1, x2, th4)
y4 = f(s4)

print("Sx4 =",s4)
print("y4 =", round(y4,4)) 
print()

s5 = sumX(w35, w45, y3, y4, th5)
y5 = f(s5)
y5 = 0.7856
print("Sx5 =",s5)
print("y5 =", round(y5,4)) 
print()


e5 =(yd5 - y5)
print("error e5 =", round(e5,4))
q5 = y5*(1-y5)*e5
print("error gradient q5 =", round(q5, 4))
q3 = y3*(1-y3)*q5*w35
print("error gradient q3 =", round(q3, 4))
q4 = y4*(1-y4)*q5*w45
print("error gradient q4 =", round(q4, 4))

print()
print("========= cal deta weight========")

dw35 = a*y3*q5
dw45 = a*y4*q5
dth5 = a*(-1)*q5

print("Node 5")
print("delta w35", round(dw35, 4))
print("delta w45", round(dw45, 4))
print("delta th5", round(dth5, 4))
print("-------------------------")

dw13 = a*x1*q3
dw23 = a*x2*q3
dth3 = a*(-1)*q3

print("Node 3")
print("delta w13", round(dw13, 4))
print("delta w23", round(dw23, 4))
print("delta th3", round(dth3, 4))
print("-------------------------")
dw14 = a*x1*q4
dw24 = a*x2*q4
dth4 = a*(-1)*q4

print("Node 4")
print("delta w14", round(dw14, 4))
print("delta w24", round(dw24, 4))
print("delta th4", round(dth4, 4))
print("-------------------------")

print()
print("====================== update all weight =======")
w13 = w13+dw13
w23 = w23+dw23
th3 = th3+dth3

w14 = w14+dw14
w24 = w24+dw24
th4 = th4+dth4

w35 = w35+dw35
w45 = w45+dw45
th5 = th5+dth5

print("w13", round(w13, 4))
print("w23", round(w23, 4))
print("th3", round(th3, 4))
print("-------------------------")
print("w14", round(w14, 4))
print("w24", round(w24, 4))
print("th4", round(th4, 4))
print("-------------------------")
print("w35", round(w35, 4))
print("w45", round(w45, 4))
print("th5", round(th5, 4))


























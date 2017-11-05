import math
def f(x):
    a = 35
    b = 1.22
    c = 2
    return a*math.exp( -(x-b)*(x-b)/(2*c*c))

def rangeX(x,maxX, a, b):
    return a + (x/maxX)*(b-a)

a = 0.5
b = 2.5
print( rangeX( 13, 15, a, b), f(rangeX( 13, 15, a, b)))
print( rangeX( 4, 15, a, b), f(rangeX( 4, 15, a, b)))
print( rangeX( 11, 15, a, b), f(rangeX( 11, 15, a, b)))
print( rangeX( 8, 15, a, b), f(rangeX( 8, 15, a, b)))

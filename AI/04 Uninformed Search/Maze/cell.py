from p5 import *
import math
import random

class Cell:
    def __init__(self, i, j, size, map):
        self.i = i
        self.j = j
        self.size = size
        self.visited = False
        self.map = map
        self.walls = [True, True, True, True]
    
    def show(self):
        x = self.j * self.size
        y = self.i * self.size

        if (self.visited):
            no_stroke()
            fill(0, 255, 0, 100)
            rect((x, y) , self.size, self.size)
        
        stroke(255)
        if self.walls[0]:
            line((x, y), (x+self.size, y))
        if self.walls[1]:
            line((x+self.size, y), (x+self.size, y+self.size))
        if self.walls[2]:
            line((x, y+self.size), (x+self.size, y+self.size))
        if self.walls[3]:
            line((x, y), (x, y+self.size))
        
        
        

    def checkNeigbhors(self):
        neighbor = []
        map = self.map
        top = map.get(self.i - 1, self.j)
        if top and not top.visited:
            neighbor.append(top)
        bottom = map.get(self.i + 1, self.j)
        if bottom and not bottom.visited:
            neighbor.append(bottom)
        left = map.get(self.i, self.j-1);
        if left and not left.visited:
            neighbor.append(left)
        right = map.get(self.i, self.j+1);
        if right and not right.visited:
            neighbor.append(right)

        N = len(neighbor)
        if N > 0:
            r = math.floor( random.randint(0, N - 1) )
            return neighbor[r]
        else:
            return None

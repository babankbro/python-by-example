from p5 import *
import random

class Cell:

    def __init__(self, i, j, size):
        self.i = i #x
        self.j = j #y
        self.size = size
        self.isWall = False
        if random.random() < 0.3:
            self.isWall = True

        self.f = 0
        self.g = 0
        self.h = 0
        self.previous = None

    def show(self, color):
        x = self.i * self.size
        y = self.j * self.size
        if self.isWall:
            fill(0)
        else:
            fill(color[0], color[1], color[2])
        rect(  (x, y), self.size, self.size )

    def getNode(self,cells, i, j, nCol):
        return cells[i + nCol*j]

    def createNeighbors(self, cells, nRow, nCol):
        neighbors = []
        j = self.j
        i = self.i

        if j < nCol-1:
            node = self.getNode(cells, i, j+1, nCol)
            neighbors.append(node)
        if j > 0:
            node = self.getNode(cells, i, j-1, nCol)
            neighbors.append(node)
        if i < nRow-1:
            node = self.getNode(cells, i+1, j, nCol)
            neighbors.append(node)
        if i > 0:
            node = self.getNode(cells, i-1, j, nCol)
            neighbors.append(node)
        
##        if j < nCol-1 and i < nRow-1:
##            node = self.getNode(cells, i+1, j+1, nCol)
##            neighbors.append(node)
##        if j > 0 and i < nRow-1:
##            node = self.getNode(cells, i+1, j-1, nCol)
##            neighbors.append(node)
##        if j < nCol-1 and i > 0:
##            node = self.getNode(cells, i-1, j+1, nCol)
##            neighbors.append(node)
##        if j> 0 and i > 0:
##            node = self.getNode(cells, i-1, j-1, nCol)
##            neighbors.append(node)
        
        return neighbors

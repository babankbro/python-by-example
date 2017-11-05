from p5 import *
from cell import *
from heapq import *
import math

width = 800
nCol = 40
nRow = 40
cells = []

start = None
end = None
openSet = [] 
closedSet = []
path = []
finish = False
current = None

def setup():
    size(width, width)
    sizeCell = width/nCol
    for j in range(nCol):
        for i in range(nRow):
            cell = Cell(i, j, sizeCell)
            cells.append(cell)
            #print(i, j, i + j*nCol)
    background(60)
    i = nCol -1
    j = 0
    end = cells[i + j*nCol]
    global end
    i = 0
    j = 0
    start = cells[i + j*nCol]
    #openSet.append(start)
    heappush(openSet, (0, start))
    

def update_path():
    path.clear()
    global current
    node = current
    while node != None:
        path.append(node)
        node = node.previous
        
def isInOpenSet(node):
    for value, n in openSet:
        if n == node:
            return True
    return False

def update_astar():
    global current, finish
    if len(openSet) > 0:
        value, current = heappop(openSet)

        closedSet.append(current)

##        print(end.i, end.j)
        if current == end:
            finish = True
        else:
          
            neighbors = current.createNeighbors(cells, nRow, nCol)
            #print(len(neighbors))
            for node in neighbors:
                if node in closedSet or node.isWall:
                    continue
                
                h = abs(node.i - end.i) + abs(node.j - end.j) + node.i*0.0001 + node.j*0.01
                g = current.g + 1
                f = g + h

                if isInOpenSet(node):
                    if f < node.f:
                        node.f = f
                        node.g = g
                        node.h = h
                        node.previous = current
                else:
                    node.f = f
                    node.g = g
                    node.h = h
                    node.previous = current
                    #print(f, node.i, node.j)
                    heappush(openSet, (f, node))
    update_path()

def draw():
    if not finish:
        update_astar()
    
    background(60)
    #print(len(path))
    
    for cell in cells:
        cell.show((255, 255, 255))

    for vaule, cell in openSet:
        cell.show((0, 255, 0))

    for cell in closedSet:
        cell.show((255, 0, 0))

    for cell in path:
        cell.show((0, 0, 255))

run()

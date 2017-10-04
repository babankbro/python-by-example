from cell import *

class MazeMap:
    def __init__(self, nRow, nCol, sizeCell):
        self.nRow = nRow
        self.nCol = nCol
        self.sizeCell = sizeCell
        self.cells = []
        self.pathStack = []
        
        for i in range(nRow):
            for j in range(nCol):
                cell = Cell(i, j, sizeCell, self)
                self.cells.append(cell)
        
        self.current =self.cells[0]
        self.current.visited = True
        self.pathStack.append(self.current)
        
    def show(self):
        stroke(255)
        for cell in self.cells:
            cell.show()
        fill(0, 0, 255)
        x = self.current.j*self.sizeCell
        y = self.current.i*self.sizeCell
        rect((x, y), self.sizeCell, self.sizeCell)

    def get(self, i, j):
        if i < 0 or j < 0 or i >= self.nRow or j >= self.nCol:
            return None
        index = j + i*self.nCol
        return self.cells[index]
    
    def move(self):
        next = self.current.checkNeigbhors()
        if next != None:
            self.removeWall(next, self.current);
            self.current = next
            self.current.visited = True
            self.pathStack.append(self.current)
        else:
            if len(self.pathStack) == 0:
                return
            self.current = self.pathStack.pop()

    def removeWall(self, next, current):
        di = next.i - current.i
        dj = next.j - current.j
        if di == 1: #move down
            next.walls[0] = False
            current.walls[2] = False
        elif di == -1:
            next.walls[2] = False
            current.walls[0] = False
        elif dj == 1:
            next.walls[3] = False
            current.walls[1] = False
        else:
            next.walls[1] = False
            current.walls[3] = False






    

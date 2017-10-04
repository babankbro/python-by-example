from cell import *
from maze_map import *
from p5 import *
import time

map = None

def setup():
    global map
    width = 800
    size(width, width)
    N = 30
    sizeCell = width/N
    map =  MazeMap(N, N, sizeCell)
    
def draw():
    background(60)
    map.move()
    map.show()
    #time.sleep(0.01)
    
run()

from p5 import *
from vehicle import *
import random



screen_width = 800
nfood = 40
nposion = 20
nvehicle = 10
food = []
posion = []
vehicles = []

def generate_food():
    for i in range(nfood):
        x = random.random()*screen_width
        y = random.random()*screen_width
        food.append(Vector(x, y))

def generate_posion():
    for i in range(nposion):
        x = random.random()*screen_width
        y = random.random()*screen_width
        posion.append(Vector(x, y))
        
def generate_vehicles():
    for i in range(nvehicle):
        x = random.random()*screen_width
        y = random.random()*screen_width
        vehicles.append(Vehicle(x, y))

def draw_food():
    fill(0, 255, 0)
    for fd in food:
        circle( (fd.x, fd.y), 5)

def draw_posion():
    fill(255, 0, 0)
    for fd in posion:
        circle( (fd.x, fd.y), 5)

def setup():
    size(screen_width, screen_width)
    generate_food()
    generate_posion()
    generate_vehicles()

def draw():
    background(60)
    toRemoves = []
    for vehicle in vehicles:
        vehicle.boundaries()
        if len(food) > 0 :
            vehicle.behaviors(food, posion)
            #vehicle.eat(posion)
        else:
            target = Vector(mouse_x, mouse_y)
            vehicle.seek(target)

        vehicle.update()
        vehicle.draw()
        if vehicle.dead():
            toRemoves.append(vehicle)

    for vehicle in toRemoves:
        vehicles.remove(vehicle)

    circle( (mouse_x, mouse_y), 30)

    draw_food()
    draw_posion()
    
run()

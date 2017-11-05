from p5 import *
import numpy
import random

class Vehicle:

    def __init__(self, x, y, maxSpeed=6):
        self.acceleration = Vector(0, 0)
        self.velocity = Vector(0, -2)
        self.position = Vector(x, y)
        self.r = 10
        self.maxSpeed = maxSpeed
        self.maxforce = 0.5
        self.dna = [random.uniform(-1,1), -random.uniform(-1,1)]
        self.health =  1

    def update(self):
        self.health -= 0.002
        self.velocity += self.acceleration
        self.velocity.limit(self.maxSpeed)
        self.position += self.velocity
        self.acceleration *= 0

    def applyForce(self, force):
        self.acceleration += force

    def seek(self, target):
        desired = target - self.position

        desired.normalize()
        desired *= self.maxSpeed

        steer = desired - self.velocity
        steer.limit(self.maxforce)

        return steer

    def dead(self):
        return self.health < 0

    def steerEat(self, poslist, score):
        if len(poslist) == 0:
            return Vector(0, 0)
        minDis =  poslist[0].distance(self.position)
        closest = poslist[0]
        for pos in poslist:
            dis = pos.distance(self.position)
            if dis < minDis:
                minDis = dis
                closest = pos
                
        if minDis < 10:
            poslist.remove(closest)
            self.health += score
      
        return self.seek(closest)

    def behaviors(self, good , bad):
        steerG = self.steerEat(good, 0.2)
        steerB = self.steerEat(bad, -0.5)

        steerG *= self.dna[0]
        steerB *= self.dna[1]

        self.applyForce(steerG)
        self.applyForce(steerB)

    def boundaries(self):
        desired = None
        d = 50
        width
        if self.position.x < d:
            desired = Vector(self.maxSpeed, self.velocity.y)
        elif self.position.x > width - d:
            desired = Vector(-self.maxSpeed, self.velocity.y)
        elif self.position.y < d:
            desired = Vector(self.velocity.x,self.maxSpeed)
        elif self.position.y > width - d:
            desired = Vector(self.velocity.x, -self.maxSpeed)

        if desired != None:
            desired.normalize()
            desired *= self.maxSpeed
            steer = desired - self.velocity
            steer.limit(self.maxforce)
            self.applyForce(steer)
    

    def draw(self):
        theta = self.velocity.angle + radians(90)
        gr = lerp(0, 255, self.health)
        rd =  lerp(255, 0, self.health)
        
        fill(rd, gr, 0)
        stroke(220)
        translate(self.position.x, self.position.y)
        rotate_z(theta)
        triangle( (0, -self.r*2, 0),
                  (-self.r, self.r*2, 0),
                  (self.r, self.r*2, 0))
        
        stroke(0, 255, 0)
        line((0, 0), (0, -self.r-self.dna[0]*50))
        stroke(255, 0, 0)
        line((0, 0), (0, -self.r-self.dna[1]*50))
        
        rotate_z(-theta)
        translate(-self.position.x, -self.position.y)
        
        

        

g = 9.81
r = 1
mass = 1

def dist(x, y):
    return (x**2 + y**2)**(1/2)

def force(this, that):
    return g*(that - this)/(2*r)

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

def getforce(p):
    vertforce = g
    horforce = 0
    for d in Particle:
        if(dist(p.x - d.x, p.y - d.y) <= 2*r):
            vertforce += force(p.y, d.y)
            horforce += force(p.x, d.x)
    return vertforce, horforce

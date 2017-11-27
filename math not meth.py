g = -9.81
r = 1
mass = 1
all = []

def vectsum(x, y):
    return (x**2 + y**2)**(1/2)

def force(this, that):
    z = vectsum(this.x - that.x, this.y - that.y)
    if z > r*2:
        return -1/z**6*(this.x - that.x)/2, -1/z**6*(this.y - that.y)/2
    if z < r*2:
        return 1/z**8*(this.x - that.x)/2, 1/z**8*(this.y - that.y)/2
    else:
        return 0, 0

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        all.append(self)

    def move(self, x, y):
        self.x += x
        self.y += y

def getforce(p):
    vertforce = g
    horforce = 0
    for d in all:
        if d is not p:
            vertforce += force(p, d)[1]
            horforce += force(p, d)[0]
    return horforce, vertforce


p = Particle(0,0)
d = Particle(1,1)
print(getforce(d))

g = -9.81
r = 0.5
mass = 1
all = []

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __abs__(self):
        return (self.x**2+self.y**2)**(1/2)


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v = Vector(0, 0)
        all.append(self)

    def move(self):
        if self.x + self.v.x >= 0:
            self.x += self.v.x
        if self.y + self.v.y >= 0:
            self.y += self.v.y

    def accel(self, a):
        self.v += a

def force(self, other):
    z = Vector(self.x - other.x, self.y - other.y)
    z /= abs(z)
    z *= (1/abs(z)**5 - 1/abs(z)**7)
    return z

def getforces(p):
    f = Vector(0, g)
    for d in all:
        if d is not p:
            f += force(p, d)
    return f


p = Particle(0,0)
d = Particle(1,1)
f = Particle(1,0)
print(d.x, d.y)
d.accel(getforces(d))
d.move
print(d.x, d.y)

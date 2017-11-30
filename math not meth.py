mol = []
g = -0.025

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x,y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __abs__(self):
        return (self.x**2+self.y**2)**(1/2)

class Particle:
    def __init__(self, x, y):
        self.x, self.y, self.v = x, y, Vector(0, 0)
        mol.append(self)

    def move(self):
        if self.x + self.v.x >= 0:
            self.x += self.v.x
        if self.y + self.v.y >= 0:
            self.y += self.v.y

    def acc(self):
        a = Vector(0, g)
        for i in mol:
            if i is not self:
                z = Vector(i.x - self.x, i.y - self.y)
                r = a - z / abs(z) ** 8 + z / abs(z) ** 6
                if (abs(r) < 0.9*abs(z)) | (abs(r) > 1.1*abs(z)):
                    a = r
        self.v += a


p = Particle(0, 0)
d = Particle(1.2, 0)
for i in range(100):
    d.acc()
    d.move()
    print(d.x, d.y)

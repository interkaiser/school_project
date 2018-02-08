g = 1
things = []


class Particle:
    def __init__(self, x, y):
        self.x, self.y, self.vx, self.vy, self.ax, self.ay = x, y, 0, 0, 0, g
        things.append(self)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vx += self.ax
        self.vy += self.ay

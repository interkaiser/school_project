from graphics import *

frames = []
mol = []
g = -1


class Particle:
    def __init__(self, x, y):
        self.x, self.y, self.vx, self.vy, self.ax, self.ay = x, y, 0, 0, 0, g
        mol.append(self)

    def move(self):
        self.x, self.y = min(self.x + self.vx, 255), min(self.y + self.vy, 255)
        self.x, self.y = max(self.x, 0), max(self.y, 0)
        for i in mol:
            if i is not self:
                if i.x != self.x:
                    self.ax += 1 / (i.x - self.x) ** 5 - 400 / (i.x - self.x) ** 7
                if i.y != self.y:
                    self.ay += 1 / (i.y - self.y) ** 5 - 400 / (i.y - self.y) ** 7
        self.vx += self.ax
        self.vy += self.ay
        minx = 255
        vx = 0
        miny = 255
        vy = 0
        d = 255 * 2 ** 0.5
        for i in mol:
            dist = ((self.x - i.x) ** 2 + (self.y - i.y) ** 2) ** 0.5
            if (i is not self) & (d < dist):
                d = dist
                minx = i.x - self.x
                miny = i.y - self.y
                vx = i.vx
                vy = i.vy
        if ((self.x - minx) * (self.vx - vx) < 0) & ((self.y - miny) * (self.vy - vy) < 0) and (d < (
                (self.vx - vx) ** 2 + (self.vy - vy) ** 2) ** 0.5):
            self.vx = 2*(minx - self.x) - self.vx
            self.vy = 2 * (miny - self.y) - self.vy

def render():
    for i in range(100):  # rendering
        pts = []
        for i in mol:
            pts.append({'x': i.x, 'y': i.y})
            i.move()
        frames.append(pts)

def play():
    for f in frames:
        for i in win.items:
            win.delItem(i)
        for p in f:
            prt = Circle(p, 10)
            prt.setFill('black')
            prt.draw(win)
        time.sleep(0.04)


win = GraphWin("Simulation", 255, 255)
win.setBackground('white')
p = Particle(2, 0)
q = Particle(0, 0)
render()
win.getMouse()
play()
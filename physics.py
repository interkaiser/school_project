from tkinter import *
from random import *
scale = 500
g = 10
step = 0.02
size = 1
r = scale / 100 * size
n = 20
total = 10
things = []


class Particle:
    def __init__(self, x, y):
        self.shape = canvas.create_oval(x - r, y - r, x + r, y + r, fill='black')
        self.x, self.y = x, y
        self.vx, self.vy = 0, 0

    def move(self):
        self.vy += g * step
        if (self.x > scale - r) or (self.x < r):
            self.vx *= -1
        if (self.y > scale - r) or (self.y < r):
            self.vy *= -1
        for i in things:
            d = (self.x - i.x) ** 2 + (self.y - i.y) ** 2
            if (d > 0) and (d < r * r):
                self.vx += i.vx * (self.y - i.y) / d + i.vy * (self.x - i.x) / d
                self.vy += i.vy * (self.x - i.x) / d + i.vx * (self.y - i.y) / d
        self.x += self.vx
        self.y += self.vy


def move(t):
    canvas.delete(ALL)
    for i in things:
        i.move()
        canvas.create_oval(i.x - r, i.y - r, i.x + r, i.y + r, fill='black')
    if t < total:
        canvas.after(int(step * 1000), lambda: move(t + step))


frame = Tk()
canvas = Canvas(frame, width=scale, height=scale, background="white")
canvas.grid()
for g in range(n):
    things.append(Particle(randint(r, scale - r), randint(r, scale - r)))
move(0)
frame.mainloop()

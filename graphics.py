from tkinter import *
from physics import *


def create(event):
    canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, fill="black")
    things.append(Particle(event.x, event.y))


def start(event):
    canvas.delete(ALL)
    for p in things:
        p.move()
        canvas.create_oval(p.x - 10, p.y - 10, p.x + 10, p.y + 10, fill="black")



root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", create)
canvas.bind("<Button-3>", start)
root.mainloop()

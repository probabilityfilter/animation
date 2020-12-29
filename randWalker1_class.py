# single pt random walker in 2D

from graphics import *
import random, time

win = GraphWin("Walkers 2D", 600, 600)

class walker:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        # self.win = win
        
    def create(self):
        r = random.randrange(256)
        b = random.randrange(256)
        g = random.randrange(256)
        self.color = color_rgb(r, g, b)
        # r=2
        self.circle = Circle(Point(self.x,self.y), 2)
        self.circle.setFill(self.color)
        self.circle.setOutline(self.color)
        self.circle.draw(win)
    def move(self):
        # for t in range(100):
        ptStart = self.circle.getCenter()
        time.sleep(.05)
        self.circle.move(random.randrange(-10, 10),random.randrange(-10, 10))
        ptEnd = self.circle.getCenter()
        line = Line(ptStart,ptEnd)
        line.setOutline(self.color)
        line.draw(win)

n = 10
w=[0] * n
for i in range(n):
    w[i] = walker(300,300)
    w[i].create()
for t in range(100):
    for i in range(n):
        w[i].move()

win.getMouse()
win.close()
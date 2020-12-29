# single pt random walker in 2D

from graphics import *
import random, time

win = GraphWin("Moving Circles", 600, 600)

#  function not needed
def drawObject(x,y,r):    
    # radius = random.randrange(3, 40)
    xx = x + random.randrange(-10, 10)
    yy = y + random.randrange(-10, 10)

    circle = Circle(Point(xx,yy), r)
    circle.setFill(color)
    circle.draw(win)
    time.sleep(.05)
    
    # win.getMouse()
    # win.close()
    return(xx,yy)
#  function not needed

r = random.randrange(256)
b = random.randrange(256)
g = random.randrange(256)
color = color_rgb(r, g, b)
x = 300 #random.randrange(5, 295)
y = 300 #random.randrange(5, 295)
r=2
circle = Circle(Point(x,y), r)
circle.setFill(color)
circle.draw(win)

while win.getMouse:
    # (x,y) = drawObject(x,y,10)
    ptStart = circle.getCenter()
    time.sleep(.05)
    circle.move(random.randrange(-10, 10),random.randrange(-10, 10))
    ptEnd = circle.getCenter()
    line = Line(ptStart,ptEnd)
    line.draw(win)

    
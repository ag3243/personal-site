'''
TurtleShapes.py

@author: Aryan Garg
'''

import turtle, BoundingBox

def drawOneShape(turt, size):
    """
    Draws a single geometrical shape, in this case a square. The parameter
    turt will be the name of the turtle created below, and the size
    parameter will be the length of each side.
    """
    for i in range(4):
        turt.forward(size)
        turt.right(90)
def drawOneSmallHouse(turt, size):
    """
    Draws a small, multicolored house with 2 shapes:
    a triangle and a square.
    """
    #square base
    turt.color('red')
    for i in range(4):
        turt.forward(size)
        turt.right(90)
    #triangle roof
    turt.color('blue')
    turt.forward(size)
    turt.color('green')
    turt.left(135)
    turt.forward(size/1.4)
    turt.color('yellow')
    turt.left(90)
    turt.forward(size/1.4)

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    #create turtle and set speed
    boss = turtle.Turtle()
    boss.speed(0)
    #draw first shape
    drawOneShape(boss, 100)
    #move turtle and draw house
    boss.penup()
    boss.goto(-200,0)
    boss.pendown()
    drawOneSmallHouse(boss, 150)
    
    win.exitonclick()
    
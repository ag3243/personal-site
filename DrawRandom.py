'''
DrawRandom.py

@author: Aryan Garg
'''

import turtle, BoundingBox
import random
from TurtleShapes import drawOneShape, drawOneSmallHouse

def drawEverywhere(turt, func):
    """
    The function requires an input of how many shapes to draw,
    and then uses the image-drawing functions to draw that many
    shapes at random positions and sizes
    """
    num = int(input("How many shapes to draw?"))

    for i in range(num):
        #random position
        x = random.randint(-500, 500)
        y = random.randint(-250, 250)
        #random size
        size = random.randint(20, 175)
        #move turtle
        turt.penup()
        turt.goto(x, y)
        turt.pendown()
        #draw
        func(turt, size)

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    boss = turtle.Turtle()
    boss.speed(0)
    funcNumber = int(input("Input 0 for drawOneShape, 1 for drawOneSmallHouse"))
    if funcNumber == 0:
        func = drawOneShape
    else:
        func = drawOneSmallHouse
    #draw shapes
    drawEverywhere(boss, func)

    win.exitonclick()
    
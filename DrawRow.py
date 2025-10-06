'''
DrawRow.py

@author: Aryan Garg
'''

import turtle, BoundingBox
from TurtleShapes import drawOneSmallHouse

def drawRowsOfRows(turt, func):
    """
    Draw 10 rows of shapes using the parameter func to draw images.
    Each row should have 10 images with the same size in different
    y coordinates.
    """
    #positions
    y = 250
    row_space = 50
    col_space = 50
    x = -300
    #shape sizes
    size = 10
    increase = 3

    #create rows
    for row in range(10):
        final_y = y - row * 1.2 * row_space
        final_size = size + row * increase

        for i in range(10):
            final_x = x + i * col_space
            turt.penup()
            turt.goto(final_x, final_y - final_size/2)
            turt.setheading(0)
            turt.pendown()
            func(turt, final_size)

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    boss = turtle.Turtle()
    boss.speed(0)
    ## CALL FUNCTIONS HERE
    drawRowsOfRows(boss, drawOneSmallHouse)
    win.exitonclick()
    
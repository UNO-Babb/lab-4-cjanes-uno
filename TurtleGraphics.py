#TurtleGraphics.py
#Name: Colton Janes
#Date: 02/15/2025
#Assignment: Lab 4 - Turtle

import turtle
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(polly, sides):
    for s in range(sides):
        polly.forward(50)
        polly.right(360/sides)
        
def fillCorner(carol, corner):
    drawSquare(carol, 100)
    
    if corner == 1:
        carol.begin_fill()
        drawSquare(carol, 50)
        carol.end_fill()
    
    elif corner == 2:
        carol.forward(50)
        carol.begin_fill()
        drawSquare(carol, 50)
        carol.end_fill()
    
    elif corner == 3:
        carol.right(90)
        carol.up()
        carol.forward(50)
        carol.left(90)
        carol.down()
        carol.begin_fill()
        drawSquare(carol, 50)
        carol.end_fill()
    
    elif corner == 4:
        carol.up()
        carol.forward(50)
        carol.right(90)
        carol.forward(50)
        carol.left(90)
        carol.down()
        carol.begin_fill()
        drawSquare(carol, 50)
        carol.end_fill()

def squaresInSquares(sam, num):
    size = 10
    
    for sq in range(num):
        sam.up()
        sam.goto(-size / 2, size / 2)
        sam.down()
        drawSquare(sam, size)
        size = size + 20
                
def main():
    myTurtle = turtle.Turtle()
        
    #drawSquare(myTurtle, 100)
    
    ##drawPolygon(turtle, sides)
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 3) #draws a triangle

    ##fillCorner(turtle, corner)
    #fillCorner(myTurtle, 1) #draws a square with top left corner filled in.
    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    #fillCorner(myTurtle, 4) #draws a square bottom right corner filled in.

    ##squaresInSquares(turtle, num)
    #squaresInSquares(myTurtle, 1) #draws 1 set of concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares
    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    squaresInSquares(myTurtle, 15) #draws 15 concentric squares

main()

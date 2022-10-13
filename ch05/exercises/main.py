import turtle

def drawSquare(myTurtle=None,side_length=0):
    for i in range (4):
      myTurtle.forward(side_length)
      myTurtle.left(90)


leo = turtle.Turtle



drawSquare(leo, 50)
      
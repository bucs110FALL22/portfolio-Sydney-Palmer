# importing turtle and setting the screen
import turtle
window = turtle.Screen()
Turtle = turtle.Turtle()
Turtle.color('Blue')
window.bgcolor('lightgray')

# function that draws base of house
def draw_base(color):  
  turtle.screensize(500,500)
  Turtle.speed(1)
  Turtle.pencolor(color)
  Turtle.fillcolor(color)
  Turtle.begin_fill()
  for i in range(4):
    Turtle.forward(200)
    Turtle.right(90)

  Turtle.end_fill()

# function that draws roof of house
def draw_roof(color):
  Turtle.speed(1)
  Turtle.pencolor(color)
  Turtle.fillcolor(color)
  Turtle.begin_fill()  
  for i in range(3):
    Turtle.forward(200)
    Turtle.right(-120)
  
  Turtle.end_fill()

  
# function that draw door of house
def draw_door(color):
  Turtle.up()
  Turtle.goto(80,-100)
  Turtle.down()
  Turtle.speed(1)
  Turtle.pencolor(color)
  Turtle.fillcolor(color)
  Turtle.begin_fill()  
  for i in range(2):
    Turtle.forward(50)
    Turtle.right(90)
    Turtle.forward(100)
    Turtle.right(90)

  Turtle.end_fill()

  
# function that draw a doorknob on house
def draw_doorknob(color):
  Turtle.up()
  Turtle.goto(120,-150)
  Turtle.down()
  Turtle.speed(1)
  Turtle.pencolor(color)
  Turtle.fillcolor(color)
  Turtle.begin_fill()
  Turtle.circle(3)
  Turtle.end_fill()  


# function that draws both windows of the house
def draw_windows(color):

  Turtle.up()
  Turtle.goto(20,-20)
  Turtle.down()
  Turtle.speed(1)
  Turtle.pencolor(color)
  for i in range(4):
    Turtle.forward(50)
    Turtle.right(90)

  Turtle.up()
  Turtle.goto(140,-20)
  Turtle.down()
  Turtle.speed(1)
  Turtle.pencolor(color)
  for i in range(4):
    Turtle.forward(50)
    Turtle.right(90) 
   

  
# function that draws the lines of the windows
def draw_lines(color):
  Turtle.up()
  Turtle.goto(165,-20)
  Turtle.down()
  Turtle.right(90)
  Turtle.speed(1)
  Turtle.pencolor(color)
  Turtle.forward(50)
  Turtle.up()
  
  Turtle.goto(140,-45)
  Turtle.down()
  Turtle.left(90)
  Turtle.speed(1)
  Turtle.pencolor(color)
  Turtle.forward(50)
  Turtle.up()

  
# function that draws the lines of the windows  
def draw_lines1(color):
  Turtle.up()
  Turtle.goto(45,-20)
  Turtle.down()
  Turtle.right(90)
  Turtle.speed(1)
  Turtle.pencolor(color)
  Turtle.forward(50)
  Turtle.up()

  Turtle.goto(20,-45)
  Turtle.down()
  Turtle.left(90)
  Turtle.speed(1)
  Turtle.pencolor(color)
  Turtle.forward(50)
  Turtle.up()

def draw_moon(color):
  Turtle.up()
  Turtle.goto(-250,150)
  Turtle.down()
  Turtle.speed(1)
  Turtle.pencolor(color)
  Turtle.fillcolor(color)
  Turtle.begin_fill()
  Turtle.circle(40)
  Turtle.end_fill()  

# function to give you candy (function using a return)
def giving_candy(num):
  total = num + 1
  return total 
  
    
# all the functions put together to make the house and give you candy
def main():
  draw_base("Black")
  draw_roof("Orange")
  draw_door("Purple")
  draw_doorknob("Red")
  draw_windows("Blue")
  draw_lines("Blue")
  draw_lines1("Blue")
  draw_moon("White")
  print ("This house loves halloween, go trick or treat at their house and they'll ask you how much candy you want! If you have a really good costume they'll do something special, go find out!!")
  result = giving_candy(89)
  print ("Here is an extra candy because I LOVE your costume, so now you have", result, "candies")




#calling the function
main()

window.exitonclick()
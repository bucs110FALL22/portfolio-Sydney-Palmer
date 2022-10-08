import turtle #1. import modules
import random
import time
import math
import pygame

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here

value = random.randrange(1,101)
michelangelo.forward(value)
value_2 = random.randrange(1,101)
leonardo.forward(value_2)

leonardo.goto(-100,20)
michelangelo.goto(-100,20)


for i in range(10):
  michelangelo.forward(random.randrange(0,11))
  leonardo.forward(random.randrange(0,11))


michelangelo.goto(-100,20)
leonardo.goto(-100,20)
                 


# PART B - complete part B here
import turtle #1. import modules
import random



# PART B - complete part B here
import pygame
pygame.init()
window = pygame.display.set_mode()



coords = []
num_sides = 3
side_length = 50
offset = 100

for i in range (num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  points = (x,y)
  coords.append(points)
  

pygame.time.wait(2500)
pygame.draw.polygon(window, "red", coords)
pygame.display.flip()
window.fill("black")


coords = []
num_sides = 4
side_length = 50
offset = 100

for i in range (num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  points= (x,y)
  coords.append(points)

pygame.time.wait(2500)
pygame.draw.polygon(window, "red", coords)
pygame.display.flip()
window.fill("black")

coords = []
num_sides = 6
side_length = 50
offset = 100

for i in range (num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  points = (x,y)
  coords.append(points)
  
pygame.time.wait(2500)
pygame.draw.polygon(window,"red", coords)
pygame.display.flip()
window.fill("black")

coords = []
num_sides = 9
side_length = 50
offset = 100

for i in range (num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  points = (x,y)
  coords.append(points)
  
pygame.time.wait(2500)
pygame.draw.polygon(window,"red", coords)
pygame.display.flip()
window.fill("black")

coords = []
num_sides = 360
side_length = 50
offset = 100

for i in range (num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  points = (x, y)
  coords.append(points)

pygame.time.wait(2500)
pygame.draw.polygon(window,"red", coords)
pygame.display.flip()
pygame.time.wait(2500)
window.fill("black")

window.exitonclick() 


 
import pygame
import random
import math
pygame.init()


#Part A
window_height = 500
window_width = 500
window = pygame.display.set_mode([window_height,window_width])

x = 250
y = 250
center = (x,y)
window.fill([0,128,255])
pygame.draw.circle(window, "pink", center, 250)
x2 = 0
y2 = 250
start_pos = (x2,y2)
x3 = 500
y3 = 250
end_pos = (x3, y3)
pygame.draw.line(window, "black", start_pos, end_pos, width = 2)
x4 = 250
y4 = 500
start_pos2 = (x4, y4)
x5 = 250
y5 = 0
end_pos2 = (x5, y5)
pygame.draw.line(window,"black",start_pos2, end_pos2, width = 2)
pygame.display.flip()



#Part B
for i in range (10):
  value = random.randrange(0, window_width)
  value2 = random.randrange(0, window_height)    
  coordinates = (value, value2)
  distance_from_circle = math.hypot (value-x, value2-y)
  is_in_circle = distance_from_circle <= window_width/2  
  if is_in_circle == False: 
      pygame.draw.circle(window,"red",coordinates,3)
      pygame.display.flip()
      pygame.time.wait(2500)
  if is_in_circle == True:
    pygame.draw.circle(window,"green",coordinates,3)
    pygame.display.flip()
    pygame.time.wait(2500)
  print (coordinates)
  print (distance_from_circle)
  print (is_in_circle)


#Part C
window.fill("white")
choice = ""
mouse_position = pygame.mouse.get_pos()
blue = pygame.draw.rect(window,"Blue",(50,60,100,50) )
red = pygame.draw.rect(window,"Red",(180,60,100,50) )
pygame.display.flip()
pygame.time.wait(2500)

print ("Who will win, red pr blue?")
pygame.time.wait(6000)

window.fill("white")
pygame.display.flip()
pygame.time.wait(2500)

window_height = 500
window_width = 500
window = pygame.display.set_mode([window_height,window_width])

x = 250
y = 250
center = (x,y)
window.fill([0,128,255])
pygame.draw.circle(window, "pink", center, 250)
x2 = 0
y2 = 250
start_pos = (x2,y2)
x3 = 500
y3 = 250
end_pos = (x3, y3)
pygame.draw.line(window, "black", start_pos, end_pos, width = 2)
x4 = 250
y4 = 500
start_pos2 = (x4, y4)
x5 = 250
y5 = 0
end_pos2 = (x5, y5)
pygame.draw.line(window,"black",start_pos2, end_pos2, width = 2)
pygame.display.flip()

players = ["red","blue"]
r_score = 0
b_score = 0

for i in range (10):
  for player in players:
    value = random.randrange(0, window_width)
    value2 = random.randrange(0, window_height)    
    coordinates = (value, value2)
    distance_from_circle = math.hypot (value-x, value2-y)
    is_in_circle = distance_from_circle <= window_width/2  
    if is_in_circle == True:
      print (player, "hit in the circle")
      pygame.draw.circle(window,player,coordinates,3)
      pygame.draw.circle(window,player,coordinates,3)
      if player is players[0]:
        r_score += 1
      if player is players[1]:
        b_score += 1
      pygame.display.flip()
      pygame.time.wait(2500)
    if is_in_circle == False: 
      print (player, "missed the circle")
      pygame.draw.circle(window,"purple",coordinates,3)
      pygame.display.flip()
      pygame.time.wait(2500)
if i == 9:
    if r_score > b_score:
      print (players[0], "won the game")
    if b_score > r_score:
      print (players[1], "won the game")
    if b_score == r_score:
      print ("The game is tied")
    pygame.time.wait(1000)

pygame.display.flip()
pygame.time.wait(2500)

Guess = True
while Guess == True:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.pos[0] < x / 2:
        playerchoice = "red"
        Guess = False
      elif event.pos [0] > x / 2:
        playerchoice = "blue"
        Guess = False
print("Your player is",playerchoice)
pygame.display.flip()
pygame.time.wait(1000)


if Guess is playerchoice:
    print("You're right")
else:
  print("You're wrong")
pygame.time.wait(1000)


  

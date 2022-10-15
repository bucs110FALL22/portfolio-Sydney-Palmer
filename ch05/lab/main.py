import pygame

#Part A
n = 101
def part_A(n):
  count = 0
  while n != 1:
    if (n % 2 == 0):
      n =  n // 2
      print (n)
    else:
      n = (3 * n) + 1 
      print (n)
    
    count +=  1
  
#Part B
list = []
upper_limit = 20
iters = {}
for start in range(2, upper_limit + 1):
  count = 0
  
  while n != 1:
    if (n % 2 == 0):
      n =  n // 2
    else:
      n = (3 * n) + 1 
    
    count +=  1
    iters = {n:count}
    list.append(iters)
print(list)
    
#Part C 
pygame.init()
window = pygame.display.set_mode()
window.fill ("white")
pygame.display.flip()
font = pygame.font.Font(None, 16)

#variables
upper_limit = 20
iters = {}
max_so_far = 0
#max_val = 
scale = 5

for i in range(2,upper_limit + 1):
  count = 0
  while n != 1:
    if (n % 2 == 0):
      n =  n // 2 
    else:
      n = (3 * n) + 1 
    count +=  1
    iters = {n:count}
    iters.item(iters) 
    
    if iters.item >= 2:
      pygame.draw.lines(window,"black",iters.item())
      pygame.display.flip()
  

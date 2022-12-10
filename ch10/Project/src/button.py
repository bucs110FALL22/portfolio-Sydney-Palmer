import pygame

class Button:
   def __init__(bee, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     bee.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     bee.rect= bee.image.get_rect()
     bee.rect.topleft = (x,y)
     bee.clicked=False
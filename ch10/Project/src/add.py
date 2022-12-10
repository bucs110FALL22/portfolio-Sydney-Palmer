import pygame

class Add:
   def __init__(water_can_1, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     water_can_1.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     water_can_1.rect= water_can_1.image.get_rect()
     water_can_1.rect.topleft = (x,y)
     water_can_1.clicked=False
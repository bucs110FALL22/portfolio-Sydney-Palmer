import pygame
import random
#like an import for classes instead of modules
class Enemy(pygame.sprite.Sprite):
  def __init__(self):
      #just the first line you have to put in the sprite class init
      super().__init__(self) 
      # with sprite you are required to have self.image and self.rect
      self.image = pygame.image.load("")
      self.rect = self.image.get_rect()
      self.speed = 1
    
  def update(self):
    self.rect.x += random.randrange(-self.speed, self.speed+1)
    self.rect.y += random.randrange(-self.speed, self.speed+1)

import pygame
import random
#like an import for classes instead of modules
class Player(pygame.sprite.Sprite):
  def __init__(self):
      super().__init__(self) #just the first line you have to put in the sprite class init
      #rest of our model
      self.health = 3
      self.direction = 3 
      # with sprite you are required to have self.image and self.rect
      self.image = pygame.image.load("")
      self.rect = self.image.get_rect()
      self.speed = 1
  #def move(self,direction):

  def move_up(self):
    self.rect.y -= self.speed

  def move_down(self):
    self.rect.y += self.speed

  def move_right(self):
    self.rect.x += self.speed

  def move_left(self):
    self.rect.x -= self.speed

  def fight(self, component):
    return random.randrange(3)
    
    
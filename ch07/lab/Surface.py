from  Rectangle import Rectangle
class Surface:
    def __init__(self, filename, x, y, height, width):
      self.image = filename
      self.rect = Rectangle(x,y,height,width)

    def getRect(self):
      '''
      This function returns the variable self.rect a rectangle that has been made based          off of the parameters. 
      '''
      return (self.rect)
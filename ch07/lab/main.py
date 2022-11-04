from Rectangle import Rectangle
from Surface import Surface


def main():
  '''
  This function takes both the rectangle and surface module and uses it to
  make rectangles using the different parameters.These paraments effect the coordinates      of the rectangle and its height and its width. With the assert module it ensures that      the modules work by making sure the expression equals true
  '''
  r = Rectangle(10, 10, 10, 10)
  assert((r.x, r.y, r.height, r.width) == (10,10,10,10))
  r = Rectangle(-1, 1, 1, 1)
  assert((r.x, r.y, r.height, r.width) == (-1,1,1,1))
  r = Rectangle(1, -1, 1, 1)
  assert((r.x, r.y, r.height, r.width) == (1,-1,1,1))
  r = Rectangle(1, 1, -1, 1)
  assert((r.x, r.y, r.height, r.width) == (1,1,-1,1))
  r = Rectangle(1, 1, 1, -1)
  assert((r.x, r.y, r.height, r.width) == (1,1,1,-1))
  s = Surface("myimage.png", 10, 10, 10, 10)
  assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10,10,10,10))
  srect = s.getRect()
  assert(srect.x,  s.getRect().y, srect.height,  srect.width) == ((10,10,10,10))
  assert (s.image) 
  print("Test Complete!")





main()
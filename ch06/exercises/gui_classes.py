class Character:
  def __init__(self):
    self.jumps = True
    self.runs = True
    self.hat = True

class Background: 
  def __init__(sky):
    sky.clouds = True
    sky.color = "light blue"
    sky.random_blocks = True

class Ground:
  def __init__(blocks):
    blocks.color = "maroon"
    blocks.texture = True
    blocks.texture_change = False
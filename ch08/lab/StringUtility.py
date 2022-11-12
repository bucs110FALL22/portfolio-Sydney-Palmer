#Part A
class StringUtility:
  def __init__ (self,string):
    self.string = string
    
  def __str__(self):
    return self.string

  def vowels(self):
    count = 0
    vowels_list = "AEIOUaeiou"
    for char in self.string:
      if char in vowels_list:
        count += 1
        
        if count >= 5:
          count = "many"
      
    
    return count
    
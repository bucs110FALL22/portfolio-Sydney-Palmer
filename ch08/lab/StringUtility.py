#Part A
class StringUtility:
  def __init__ (self,string):
    self.string = string
    
  def __str__(self):
    return self.string

  def vowels(self):
    count = 0
    vowels = ["A","E","I","O","U","a","e","i","o","u"]
    for char in self.string:
      if char in vowels:
        count += 1
    if count >= 5:
        return "many"
    return str(count)
    
  def bothEnds(self):
    char_list = []
    input_list = []
    if len(self.string) <= 0: 
      empty = ""
      return (empty)
    else:
      for char in self.string:
        char_list.append(char)
    
      first = char_list[0]
      second = char_list[1]
      third = char_list [-2]
      fourth = char_list[-1]
      input_list.append(first)
      input_list.append(second)
      input_list.append(third)
      input_list.append(fourth)
      final = "".join([str(i) for a, i in enumerate(input_list)])

      return str(final)
      
  def fixStart(self):
    if len(self.string) >1:
      char = self.string[0]
      str = self.string
      str = str.replace(char,"*")
      str = char + str[1:]
      return (str)
    else:
      empty = ""
      return (empty)
      
  def asciiSum(self):
    str = self.string
    integer = sum(ord(char) for char in str)
    return (integer)

    
 
  
    
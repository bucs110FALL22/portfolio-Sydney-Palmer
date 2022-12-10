#str = "Animal"
#modified_str = ""
#for char in range(0,len(str)):
      #if (str[char]== str[0]):
        #modified_str += "*" 
        #print (modified_str)
      #else:
        #modified_str += str[char]
        #print(modified_str)



str = "a"
if len(str) <= 1:
  char_list = []
  for char in str:
    char_list.append(char)
  key = char_list[0]
  for i in char_list:
    str = str.replace(key,"*")
    return (str)
else:
  return (str)



  





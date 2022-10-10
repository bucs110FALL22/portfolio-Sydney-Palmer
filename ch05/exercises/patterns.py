

def star_pyramid():
  print ("How many rows do you want in your star pyramid?:")
  value = int(input(""))
  
  for i in range (1, value + 1):

    print (i * "*")
    
 
star_pyramid()


def rstar_pyramid():
  print ("How many rows do you want in your star pyramid?: ")
  value_2 = int(input(""))

  for i in range (value_2, 0, -1):

    print (i* "*")


rstar_pyramid()
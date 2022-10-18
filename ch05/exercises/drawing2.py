
#function
def draw_eq_shape(franklin, num_sides, side_length):
  angle = 360/num_sides
  for s in range(num_sides):
    franklin.forward(side_length)
    franklin.right(angle)

#driver
wn = turtle.Screen
myturtle = turtle.Turtle()
myturtle.shape("turtle")
sides = int(input("How many sides?"))
length = int(input("what is the length of one side?"))  



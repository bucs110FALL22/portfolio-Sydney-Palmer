def percentage_to_letter(score):
  if score >= 90:
    letter = "A"
  if 90 > score >= 80:
    letter = "B"
  if 80 > score >= 70:
    letter = "C"
  if 70 > score >= 60:
    letter = "D"
  if score > 60:
    letter = "F"
  return letter 
  

def is_passing(letter):
  if letter >= "C":
    answer = True
  else:
    answer = False
  return answer

  

score = float(input("What is your score?"))
var = percentage_to_letter(score)
print (var)
var_2 = is_passing(letter)
print (var_2)
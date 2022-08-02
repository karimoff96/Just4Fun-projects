# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size== "S":
  size=15
  if add_pepperoni== "Y":
    size+=2
    if extra_cheese == "N":
      print(f"Your final bill is {size} ")
    else:
      size+=1
      print(f"Your final bill is {size} ")

  else:
    if extra_cheese == "N":
      print(f"Your final bill is {size} ")
    else:
      size +=1
      print(f"Your final bill is {size} ")
  
  
if size== "M":
  size=20
  if add_pepperoni== "Y":
    size+=3
    if extra_cheese == "N":
      print(f"Your final bill is {size} ")
    else:
      size+=1
      print(f"Your final bill is {size} ")

  else:
    if extra_cheese == "N":
      print(f"Your final bill is {size} ")
    else:
      size +=1
      print(f"Your final bill is {size} ")

if size== "L":
  size=25
  if add_pepperoni== "Y":
    size+=3
    if extra_cheese == "N":
      print(f"Your final bill is {size} ")
    else:
      size+=1
      print(f"Your final bill is {size} ")

  else:
    if extra_cheese == "N":
      print(f"Your final bill is {size} ")
    else:
      size +=1
      print(f"Your final bill is {size} ")




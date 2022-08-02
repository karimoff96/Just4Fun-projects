# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a=name1.lower()
b=name2.lower()
c=a+b
x1=c.count("t")
x2=c.count("r")
x3=c.count('u')
x4=c.count("e")
x=str(x1+x2+x3+x4)
y1=c.count("l")
y2=c.count("o")
y3=c.count("v")
y4=c.count("e")
y=str(y1+y2+y3+y4)
z=int(x+y)
if z<10 or z>90:
  print(f"Your score is {z}, you go together like coke and mentos.")
elif z>40 and z<50:
  print(f"Your score is {z}, you are alright together")
else:
  print(f"Your score is {z}.")



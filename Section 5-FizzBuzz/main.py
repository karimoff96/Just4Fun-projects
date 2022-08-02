#Write your code below this row 👇
number =0
for number in range(1, 101):
  if number%3==0 and number%5!=0:
    number="fizz"
  elif number%5==0 and number%3!=0:
    number="buzz"
  elif number%5==0 and number%3==0:
    number="fizzbuzz"
    # print(number)
 
  print(number)
from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter your color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_position[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f'You have won! The {winner} turtle is the winner!')
            else:
                print(f'You have lost! The {winner} turtle is the winner!')
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()

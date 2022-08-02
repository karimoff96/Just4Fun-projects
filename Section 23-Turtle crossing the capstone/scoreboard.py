from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.setposition(-290, 270)
        self.color('black')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score} ", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER ",align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



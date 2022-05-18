from turtle import Turtle
FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1

    def write_scoreboard(self):
        self.clear()
        self.goto(-280, 270)
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=FONT)
        self.goto(0, -20)
        self.write("Press SPACE to play again", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
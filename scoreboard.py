from turtle import Turtle, Screen

ALIGNMENT = "CENTER"
FONT = ("Archive", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")

    def update_score(self):
        self.goto(x=0, y=260)
        self.clear()
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def end_game(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER.", True, align=ALIGNMENT, font=("Archive", 25, "bold"))

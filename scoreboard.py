from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Archive", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.playing = True

        with open("high_score.txt") as file:
            self.high_score = file.read()

        self.hideturtle()
        self.color("white")
        self.penup()

    def update_score(self):
        self.clear()
        self.goto(x=0, y=260)
        self.write(
            f"Score: {self.score} | High score: {self.high_score}",
            True,
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        self.save_score()

        self.score = 0
        self.update_score()

    def save_score(self):
        if self.score > int(self.high_score):
            self.high_score = self.score

            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))

    def end_game(self):
        self.playing = False
        self.save_score()
        self.color("white")
        self.goto(x=0, y=0)
        self.write("GAME OVER.", True, align="Center", font=("Archive", 25, "bold"))

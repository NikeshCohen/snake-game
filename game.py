from scoreboard import Scoreboard


class Status(Scoreboard):
    def __init__(self):
        super().__init__()
        self.playing = True

    def end_game(self):
        self.playing = False
        self.goto(x=0, y=0)
        self.write("GAME OVER.", True, align="Center", font=("Archive", 25, "bold"))

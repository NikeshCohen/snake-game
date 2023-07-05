from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("blue")
        self.shape("turtle")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 240)
        self.goto(random_x, random_y)

    def random_color(self):
        self.COLOR_LIST = [
            "blue",
            "brown",
            "cyan",
            "darkcyan",
            "darkgray",
            "gray",
            "indigo",
            "lightgray",
            "lime",
            "magenta",
            "maroon",
            "navy",
            "olive",
            "orange",
            "pink",
            "purple",
            "red",
            "seagreen",
            "skyblue",
            "teal",
            "white",
            "yellow",
        ]

        color = random.choice(self.COLOR_LIST)

        return color

import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        turtle.colormode(255)
        self.color(self.random_color())
        self.shape("turtle")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 240)
        self.goto(random_x, random_y)

    def random_color(self):
        red = random.randint(50, 255)
        green = random.randint(50, 255)
        blue = random.randint(50, 255)

        color_tuple = (red, green, blue)

        return color_tuple

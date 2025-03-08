from turtle import Turtle

class PlayerTurtle(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.color("black")
        self.shapesize(0.8)
        self.blit_turtle()

    def blit_turtle(self):
        self.speed(0)
        self.penup()
        self.goto(0, -220)
        self.setheading(90)

    def up(self):
        self.forward(10)

    def reset_turtle(self):
        self.clear()
        self.goto(0, -220)
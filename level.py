from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.level = 1
        self.finish_line()
        self.write(f"Level {self.level}", False, "center", ("Courier", 15, "bold"))

    def update_level(self):
        self.level += 1
        self.clear()
        self.finish_line()
        self.write(f"Level {self.level}", False, "center", ("Courier", 15, "bold"))

    def finish_line(self):
        self.color("grey")
        self.pensize(5)
        self.penup()
        self.goto(-235, 215)
        self.pendown()
        while self.xcor() <= 240:
            self.forward(10)
            self.penup()
            self.forward(20)
            self.pendown()
        self.color("black")
        self.penup()
        self.goto(0, 220)

    def  game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Courier", 15, "bold"))
from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

class Car:
    def __init__(self):
        self.cars = []
        self.min_car_speed = 5
        self.max_car_speed = 10

    def create_cars(self):
        prob = randint(1, 6)
        if prob == 1:
           new_car = Turtle("square")
           new_car.speed(0)
           new_car.shapesize(0.8, 1.5)
           new_car.color(choice(COLORS))
           new_car.penup()
           offset_x = randint(250, 300)
           offset_y = randint(-200, 200)
           new_car.goto(offset_x, offset_y)
           self.cars.append(new_car)

    def move(self):
        self.create_cars()
        for cr in self.cars:
            if cr.xcor() <= -250:
                cr.hideturtle()
                self.cars.remove(cr)
            else:
                cr.backward(randint(self.min_car_speed, self.max_car_speed))
from turtle import Screen
from time import sleep
from car import Car
from player_turtle import PlayerTurtle
from level import Level

screen = Screen()
screen.setup(500, 500)
screen.title("TURTLE CROSSING GAME")
screen.tracer(0)

car = Car()
turtle = PlayerTurtle()
level = Level()

screen.listen()
screen.onkey(turtle.up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    car.move()

    for cr in car.cars:
        if turtle.distance(cr) < 20:
            game_is_on = False
            level.game_over()

    if turtle.ycor() >= 210:
        level.update_level()
        turtle.reset_turtle()
        car.min_car_speed += 5
        car.max_car_speed += 5

screen.exitonclick()
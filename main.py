import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from score import Score

screen = Screen()
screen.setup(width=600, height=600)

screen.title("Crossing Game")
screen.tracer(0)

car_manager = CarManager()
player = Player()
score = Score()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    

    #Detect collision of turtle with upper wall
    if player.ycor() > 280:
        player.reset_position()
        score.update_score()
        car_manager.increase_speed()

    #Detect collision with car - you must show the object, in this case car_manager.all_cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()
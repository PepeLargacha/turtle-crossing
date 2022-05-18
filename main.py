import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()

def inicial_setup():
    screen.clear()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    global scoreboard, car_manager,player
    scoreboard = Scoreboard()
    car_manager = CarManager()
    player = Player()

    screen.listen()
    screen.onkeypress(player.move_up, 'Up')

def round():
    inicial_setup()
    game_is_on = True
    generate_car = True
    counter = 0
    scoreboard.write_scoreboard()
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        if generate_car:
            car_manager.create_cars()
            generate_car = False
        elif counter > (8 - scoreboard.level):
            generate_car = True
            counter = 0
        else:
            counter += 1
        car_manager.move_cars()

        for car in car_manager.cars:
            if car.distance(player) < 19:
                print(car.pos(), player.pos())
                scoreboard.game_over()
                game_is_on = False

        if player.finish_line():
            scoreboard.increase_level()
            scoreboard.write_scoreboard()
            player.new_round()
            car_manager.increase_speed()

round()
screen.onkeypress(round, 'space')

screen.exitonclick()

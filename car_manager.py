from turtle import Turtle
from random import choice
from numpy.random import choice as npchoice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_Y = [-240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20,
              0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240]
STARTING_X = [500, 460, 420, 380, 340, 300]
INICIAL_SCREEN_X = list(range(-300, 500, 20))
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.inicial_screem()


    class Cars(Turtle):

        def __init__(self):
            super().__init__()
            self.shape("square")
            self.color(choice(COLORS))
            self.shapesize(stretch_len=2)
            self.setheading(180)
            self.penup()


    def inicial_screem(self):
        for _ in range(30):
            inicial_car = self.Cars()
            inicial_car.goto(choice(INICIAL_SCREEN_X), choice(STARTING_Y))
            self.cars.append(inicial_car)

    def create_cars(self):
        quantity = npchoice([1, 2, 3, 4, 5], p=[0.5, 0.25, 0.1, 0.1, 0.05])
        for n in range(quantity):
            new_car = self.Cars()
            new_car.goto(choice(STARTING_X), choice(STARTING_Y))
            self.cars.append(new_car)

    def move_cars(self):
        for car in range(len(self.cars)-1):
            self.cars[car].fd(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

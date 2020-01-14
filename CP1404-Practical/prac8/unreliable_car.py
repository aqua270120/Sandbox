from prac6.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name , fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(0, 100)
        if random_number <= self.reliability:
            """Drive like parent Car"""
            distance_drive = super().drive(distance)
        else:
            """don't drive if number < reliability"""
            distance_drive = 0
        return distance_drive

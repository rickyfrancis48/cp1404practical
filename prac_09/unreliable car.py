import random
from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        reliability_num = random.randint(1, 100)
        if reliability_num >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven


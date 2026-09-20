import random

class Car:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed = self.speed + change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance = self.distance + self.speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"{'Registration':<15}{'Max speed':<12}{'Speed':<10}{'Distance':<12}")
        for car in self.cars:
            print(f"{car.registration:<15}{car.max_speed:<12}{car.speed:<10}{car.distance:<12.1f}")
        print()

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False

cars = []
for i in range(1, 11):
    cars.append(Car("ABC-" + str(i), random.randint(100, 200)))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while race.race_finished() == False:
    race.hour_passes()
    hours = hours + 1
    if hours % 10 == 0:
        race.print_status()

print("The race is over!")
race.print_status()
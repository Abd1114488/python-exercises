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

cars = []
for i in range(1, 11):
    cars.append(Car("ABC-" + str(i), random.randint(100, 200)))
finished = False
while finished == False:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
    for car in cars:
        if car.distance >= 10000:
            finished = True

print(f"{'Registration':<15}{'Max speed':<12}{'Speed':<10}{'Distance':<12}")
for car in cars:
    print(f"{car.registration:<15}{car.max_speed:<12}{car.speed:<10}{car.distance:<12.1f}")
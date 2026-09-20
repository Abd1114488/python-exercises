class Car:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

car = Car("ABC 123", 142)
print("Registration number:", car.registration)
print("Maximum speed:", car.max_speed, "km/h")
print("Current speed:", car.speed, "km/h")
print("Travelled distance:", car.distance, "km")
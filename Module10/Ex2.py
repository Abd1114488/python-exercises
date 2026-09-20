class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.floor = bottom

    def floor_up(self):
        self.floor = self.floor + 1
        print("Elevator is at floor", self.floor)

    def floor_down(self):
        self.floor = self.floor - 1
        print("Elevator is at floor", self.floor)

    def go_to_floor(self, target):
        while self.floor < target:
            self.floor_up()
        while self.floor > target:
            self.floor_down()

class Building:
    def __init__(self, bottom, top, elevator_count):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for i in range(elevator_count):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, number, floor):
        self.elevators[number - 1].go_to_floor(floor)

b = Building(1, 10, 3)
b.run_elevator(1, 6)
b.run_elevator(2, 3)
b.run_elevator(1, 1)
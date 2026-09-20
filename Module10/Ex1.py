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
h = Elevator(1, 10)
h.go_to_floor(5)
h.go_to_floor(1)
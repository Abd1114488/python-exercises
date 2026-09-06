import random

n_points = int(input("How many points? "))
inside = 0

i = 0
while i < n_points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside = inside + 1
    i = i + 1

pi = 4 * inside / n_points
print("Approximate pi:", pi)
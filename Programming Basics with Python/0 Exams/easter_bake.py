import math

easter_bred_count = int(input())

total_sugar = 0
total_flour = 0
max_sugar_used = 0
max_flour_used = 0

for current_easter_bred in range(1, easter_bred_count + 1):
    sugar_used = int(input())
    flour_used = int(input())
    total_sugar += sugar_used
    total_flour += flour_used
    if max_sugar_used < sugar_used:
        max_sugar_used = sugar_used
    if max_flour_used < flour_used:
        max_flour_used = flour_used

sugar_packets = math.ceil(total_sugar / 950)
flour_packets = math.ceil(total_flour / 750)

print(f"Sugar: {sugar_packets}")
print(f"Flour: {flour_packets}")
print(f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")

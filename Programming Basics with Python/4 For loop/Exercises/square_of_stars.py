number_of_stars = int(input())

for row in range(1, number_of_stars + 1):
    print("*", end="")
    for col in range(1, number_of_stars):
        print(" *", end="")
    print()

import math

day_count = int(input())
food_left = int(input())
food_per_day_dog_kg = float(input())
food_per_day_cat_kg = float(input())
food_per_day_turtle_gr = float(input())

total_food_dog = day_count * food_per_day_dog_kg
total_food_cat = day_count * food_per_day_cat_kg
total_food_turtle = (day_count * food_per_day_turtle_gr) / 1000

total_food = total_food_dog + total_food_cat + total_food_turtle
diff_food = abs(total_food - food_left)

if total_food <= food_left:
    print(f"{math.floor(diff_food)} kilos of food left.")
else:
    print(f"{math.ceil(diff_food)} more kilos of food are needed.")
import math

x_square_meters = int(input())
y_grape_per_sq_m = float(input())
z_litters_wine = int(input())
workers_count = int(input())

total_grape = x_square_meters * y_grape_per_sq_m
grape_for_wine = total_grape * 0.40
total_wine = grape_for_wine / 2.5
diff_wine = abs(total_wine - z_litters_wine)
wine_for_workers = diff_wine / workers_count

if total_wine < z_litters_wine:
    print(f"It will be a tough winter! More {math.floor(diff_wine)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(total_wine)} liters.")
    print(f"{math.ceil(diff_wine)} liters left -> {math.ceil(wine_for_workers)} liters per person.")
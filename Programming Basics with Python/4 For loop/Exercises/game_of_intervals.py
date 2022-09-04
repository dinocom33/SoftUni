hop_count = int(input())

points = 0
points_0_9 = 0
points_10_19 = 0
points_20_29 = 0
points_30_39 = 0
points_40_50 = 0
invalid_number = 0

for i in range(1, hop_count + 1):
    number = int(input())
    if 0 <= number <= 9:
        points_0_9 = points_0_9 + 1
        points = points + (number * 0.20)
    elif 10 <= number <= 19:
        points_10_19 = points_10_19 + 1
        points = points + (number * 0.30)
    elif 20 <= number <= 29:
        points_20_29 = points_20_29 + 1
        points = points + (number * 0.40)
    elif 30 <= number <= 39:
        points_30_39 = points_30_39 + 1
        points = points + 50
    elif 40 <= number <= 50:
        points_40_50 = points_40_50 + 1
        points = points + 100
    else:
        invalid_number = invalid_number + 1
        points = points / 2

points_0_9_percent = points_0_9 / hop_count * 100
points_10_19_percent = points_10_19 / hop_count * 100
points_20_29_percent = points_20_29 / hop_count * 100
points_30_39_percent = points_30_39 / hop_count * 100
points_40_50_percent = points_40_50 / hop_count * 100
invalid_number_percent = invalid_number / hop_count * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {points_0_9_percent:.2f}%")
print(f"From 10 to 19: {points_10_19_percent:.2f}%")
print(f"From 20 to 29: {points_20_29_percent:.2f}%")
print(f"From 30 to 39: {points_30_39_percent:.2f}%")
print(f"From 40 to 50: {points_40_50_percent:.2f}%")
print(f"Invalid numbers: {invalid_number_percent:.2f}%")

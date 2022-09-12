days_count = int(input())
hours_count = int(input())

total_price = 0

for current_day in range(1, days_count + 1):
    day_price = 0
    for current_hour in range(1, hours_count + 1):
        if current_day % 2 == 0 and current_hour % 2 != 0:
            current_price = 2.50
            day_price += current_price
        elif current_day % 2 != 0 and current_hour % 2 == 0:
            current_price = 1.25
            day_price += current_price
        else:
            current_price = 1
            day_price += current_price
    total_price += day_price
    print(f"Day: {current_day} - {day_price:.2f} leva")

print(f"Total: {total_price:.2f} leva")

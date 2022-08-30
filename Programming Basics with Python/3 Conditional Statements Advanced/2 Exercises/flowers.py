hrizantemi_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_holiday = input()

total_flower_count = hrizantemi_count + roses_count + tulips_count
total_flower_price = 0

if season == "Spring" or season == "Summer":
    total_flower_price = (hrizantemi_count * 2) + (roses_count * 4.10) + (tulips_count * 2.50)
    if is_holiday == "Y":
        total_flower_price = total_flower_price * 1.15
    if season == "Spring" and tulips_count > 7:
        total_flower_price = total_flower_price * 0.95
elif season == "Autumn" or season == "Winter":
    total_flower_price = (hrizantemi_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)
    if is_holiday == "Y":
        total_flower_price = total_flower_price * 1.15
    if season == "Winter" and roses_count >= 10:
        total_flower_price = total_flower_price * 0.90
if total_flower_count > 20:
    total_flower_price = total_flower_price * 0.80
total_flower_price = total_flower_price + 2

print(f"{total_flower_price:.2f}")
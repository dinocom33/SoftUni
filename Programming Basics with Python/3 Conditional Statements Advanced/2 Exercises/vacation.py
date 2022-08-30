budget = float(input())
season = input()

location = ""
place = ""
total_price = 0

if budget <=1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        total_price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        total_price = budget * 0.45
elif budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        total_price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        total_price = budget * 0.60
else:
    place = "Hotel"
    total_price = budget * 0.90
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"

print(f"{location} - {place} - {total_price:.2f}")
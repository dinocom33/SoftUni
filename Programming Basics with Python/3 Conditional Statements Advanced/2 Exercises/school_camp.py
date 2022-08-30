season = input()
group_type = input()
students_count = int(input())
night_count = int(input())

sport_type = ""
total_price = 0

if season == "Winter":
    if group_type == "boys":
        total_price = night_count * 9.60
        sport_type = "Judo"
    elif group_type == "girls":
        total_price = night_count * 9.60
        sport_type = "Gymnastics"
    elif group_type == "mixed":
        total_price = night_count * 10
        sport_type = "Ski"
elif season == "Spring":
    if group_type == "boys":
        total_price = night_count * 7.20
        sport_type = "Tennis"
    elif group_type == "girls":
        total_price = night_count * 7.20
        sport_type = "Athletics"
    elif group_type == "mixed":
        total_price = night_count * 9.50
        sport_type = "Cycling"
elif season == "Summer":
    if group_type == "boys":
        total_price = night_count * 15
        sport_type = "Football"
    elif group_type == "girls":
        total_price = night_count * 15
        sport_type = "Volleyball"
    elif group_type == "mixed":
        total_price = night_count * 20
        sport_type = "Swimming"

total_price = total_price * students_count

if 10 <= students_count < 20:
    total_price = total_price * 0.95
elif 20 <= students_count < 50:
    total_price = total_price * 0.85
elif students_count >= 50:
    total_price = total_price * 0.50

print(f"{sport_type} {total_price:.2f} lv.")
days = int(input())
type_room = input()
grade = input()

total_price = 0

if type_room == "room for one person":
    total_price = (days - 1) * 18
elif type_room == "apartment":
    if days < 10:
        total_price = ((days - 1) * 25) * 0.70
    elif 10 <= days <= 15:
        total_price = ((days - 1) * 25) * 0.65
    else:
        total_price = ((days - 1) * 25) * 0.50
elif type_room == "president apartment":
    if days < 10:
        total_price = ((days - 1) * 35) * 0.90
    elif 10 <= days <= 15:
        total_price = ((days - 1) * 35) * 0.85
    else:
        total_price = ((days - 1) * 35) * 0.80

if grade == "positive":
    total_price = total_price * 1.25
else:
    total_price = total_price * 0.90

print(f"{total_price:.2f}")
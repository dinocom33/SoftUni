budget = int(input())
season = input()
peaple_count = int(input())

expenses = 0

if season == "Spring":
    expenses = 3000
    if peaple_count <= 6:
        expenses = expenses * 0.90
    elif 7 <= peaple_count <= 11:
        expenses = expenses * 0.85
    else:
        expenses = expenses * 0.75
elif season == "Summer" or season == "Autumn":
    expenses = 4200
    if peaple_count <= 6:
        expenses = expenses * 0.90
    elif 7 <= peaple_count <= 11:
        expenses = expenses * 0.85
    else:
        expenses = expenses * 0.75
elif season == "Winter":
    expenses = 2600
    if peaple_count <= 6:
        expenses = expenses * 0.90
    elif 7 <= peaple_count <= 11:
        expenses = expenses * 0.85
    else:
        expenses = expenses * 0.75

if (peaple_count % 2 == 0) and season != "Autumn":
    expenses = expenses * 0.95

diff = abs(budget - expenses)

if budget >= expenses:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
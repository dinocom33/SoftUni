budget = float(input())
ticket_category = input()
number_people = int(input())

transport = 0
total_ticket_price = 0
money_left = 0
diff = 0

if ticket_category == "VIP":
    if 1 <= number_people <= 4:
        transport = budget * 0.75
        total_ticket_price = number_people * 499.99
        money_left = budget - transport
        diff = abs(money_left - total_ticket_price)
    elif 5 <= number_people <= 9:
        transport = budget * 0.60
        total_ticket_price = number_people * 499.99
        money_left = budget - transport
        diff = abs(money_left - total_ticket_price)
    elif 10 <= number_people <= 24:
        transport = budget * 0.50
        total_ticket_price = number_people * 499.99
        money_left = budget - transport
        diff = abs(money_left - total_ticket_price)
    elif 25 <= number_people <= 49:
        transport = budget * 0.40
        total_ticket_price = number_people * 499.99
        money_left = budget - transport
        diff = abs(money_left - total_ticket_price)
    else:
        transport = budget * 0.25
        total_ticket_price = number_people * 499.99
        money_left = budget - transport
        diff = abs(money_left - total_ticket_price)
else:
    if ticket_category == "Normal":
        if 1 <= number_people <= 4:
            transport = budget * 0.75
            total_ticket_price = number_people * 249.99
            money_left = budget - transport
            diff = abs(money_left - total_ticket_price)
        elif 5 <= number_people <= 9:
            transport = budget * 0.60
            total_ticket_price = number_people * 249.99
            money_left = budget - transport
            diff = abs(money_left - total_ticket_price)
        elif 10 <= number_people <= 24:
            transport = budget * 0.50
            total_ticket_price = number_people * 249.99
            money_left = budget - transport
            diff = abs(money_left - total_ticket_price)
        elif 25 <= number_people <= 49:
            transport = budget * 0.40
            total_ticket_price = number_people * 249.99
            money_left = budget - transport
            diff = abs(money_left - total_ticket_price)
        else:
            transport = budget * 0.25
            total_ticket_price = number_people * 249.99
            money_left = budget - transport
            diff = abs(money_left - total_ticket_price)


if money_left >= total_ticket_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
city = input()
sell_volume = float(input())

commision = 0
city_is_valid = True
sell_volume_is_valid = True

if city == "Sofia":
    if 0 <= sell_volume <=500:
        commision = sell_volume * 0.05
    elif 500 < sell_volume <= 1000:
        commision = sell_volume * 0.07
    elif 1000 < sell_volume <= 10000:
        commision = sell_volume * 0.08
    elif sell_volume > 10000:
        commision = sell_volume * 0.12
    else:
        sell_volume_is_valid = False
elif city == "Varna":
    if 0 <= sell_volume <=500:
        commision = sell_volume * 0.045
    elif 500 < sell_volume <= 1000:
        commision = sell_volume * 0.075
    elif 1000 < sell_volume <= 10000:
        commision = sell_volume * 0.10
    elif sell_volume > 10000:
        commision = sell_volume * 0.13
    else:
        sell_volume_is_valid = False
elif city == "Plovdiv":
    if 0 <= sell_volume <=500:
        commision = sell_volume * 0.055
    elif 500 < sell_volume <= 1000:
        commision = sell_volume * 0.08
    elif 1000 < sell_volume <= 10000:
        commision = sell_volume * 0.12
    elif sell_volume > 10000:
        commision = sell_volume * 0.145
    else:
        sell_volume_is_valid = False
else:
    sell_volume_is_valid = False
if sell_volume_is_valid and city_is_valid:
    print(f"{commision:.2f}")
else:
    print("error")
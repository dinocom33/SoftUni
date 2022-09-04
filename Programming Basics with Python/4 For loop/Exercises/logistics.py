cargo_count = int(input())

truck_type = ""
bus_cargo = 0
bus_price = 0
truck_cargo = 0
truck_price = 0
train_cargo = 0
train_price = 0

for i in range(1, cargo_count + 1):
    cargo_wight = int(input())
    if cargo_wight <= 3:
        truck_type = "bus"
        bus_cargo = bus_cargo + cargo_wight
        bus_price = bus_cargo * 200
    elif cargo_wight <= 11:
        truck_type = "truck"
        truck_cargo = truck_cargo + cargo_wight
        truck_price = truck_cargo * 175
    elif cargo_wight >= 12:
        truck_type = "train"
        train_cargo = train_cargo + cargo_wight
        train_price = train_cargo * 120

total_cargo = bus_cargo + truck_cargo + train_cargo
avg_price = (bus_price + truck_price + train_price) / total_cargo
bus_cargo_percent = bus_cargo / total_cargo * 100
truck_cargo_percent = truck_cargo / total_cargo * 100
train_cargo_percent = train_cargo / total_cargo * 100

print(f"{avg_price:.2f}")
print(f"{bus_cargo_percent:.2f}%")
print(f"{truck_cargo_percent:.2f}%")
print(f"{train_cargo_percent:.2f}%")

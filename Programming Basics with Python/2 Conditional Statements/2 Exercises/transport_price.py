n_km = int(input())
day_night = input()

taxi_price_per_km = 0
bus_price = n_km * 0.09
train_price = n_km * 0.06

if day_night == "day":
    taxi_price_per_km = (n_km * 0.79)
else:
    taxi_price_per_km = (n_km * 0.90)

total_taxi_price = taxi_price_per_km + 0.70

if n_km < 20:
    print(f"{total_taxi_price:.2f}")
elif n_km < 100:
    print(f"{bus_price:.2f}")
else:
    print(f"{train_price:.2f}")
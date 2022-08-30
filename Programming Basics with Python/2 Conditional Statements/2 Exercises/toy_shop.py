trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_sum = (puzzles_count * 2.60) + (dolls_count * 3) + (bears_count * 4.10) + \
            (minions_count * 8.20) + (trucks_count * 2)
total_toys_count = puzzles_count + dolls_count + bears_count + minions_count + trucks_count

if total_toys_count >= 50:
    total_sum = total_sum * 0.75

total_sum = total_sum - (total_sum * 0.10)

diff = abs(total_sum - trip_price)

if total_sum >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")

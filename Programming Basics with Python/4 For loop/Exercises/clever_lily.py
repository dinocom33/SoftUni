age = int(input())
wash_price = float(input())
toy_price = int(input())

money = 10
toy_count = 0
brother_money = 0
total_sum = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        brother_money = brother_money + 1
        total_sum = total_sum + money
        money = money + 10
    else:
        toy_count = toy_count + 1

total_toy_sum = toy_price * toy_count
final_sum = total_toy_sum + total_sum - brother_money
diff = abs(final_sum - wash_price)

if final_sum >= wash_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

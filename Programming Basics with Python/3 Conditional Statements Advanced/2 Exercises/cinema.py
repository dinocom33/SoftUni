screening_type = input()
rows = int(input())
columns = int(input())

income = 0
capacity = rows * columns

if screening_type == "Premiere":
    income = capacity * 12
elif screening_type == "Normal":
    income = capacity * 7.50
elif screening_type == "Discount":
    income = capacity * 5

print(f"{income:.2f} leva")

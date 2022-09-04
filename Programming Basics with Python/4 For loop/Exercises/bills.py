months = int(input())

month_water_bill = 20
month_internet_bill = 15
month_electricity_bill = 0
total_electricity_bill = 0
total_water_bill = 0
total_internet_bill = 0
month_misc_bill = 0
total_misc_bill = 0



for i in range(1, months + 1):
    electricity_bill = float(input())
    month_electricity_bill = electricity_bill
    total_electricity_bill = total_electricity_bill + month_electricity_bill
    month_misc_bill = (electricity_bill + 20 + 15) * 1.2
    total_misc_bill = total_misc_bill + month_misc_bill


total_water_bill = months * 20
total_internet_bill = months * 15
avg_bill = (total_electricity_bill + total_water_bill + total_internet_bill + total_misc_bill) / months

print(f"Electricity: {total_electricity_bill:.2f} lv")
print(f"Water: {total_water_bill:.2f} lv")
print(f"Internet: {total_internet_bill:.2f} lv")
print(f"Other: {total_misc_bill:.2f} lv")
print(f"Average: {avg_bill:.2f} lv")

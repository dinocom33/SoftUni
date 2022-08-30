nylon = int(input())
paint = int(input())
thinner = int(input())
working_hours = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5

nylon_sum = (nylon + 2) * nylon_price
paint_sum = (paint + (paint * 0.1)) * paint_price
thinner_sum = thinner * thinner_price
materials_total_sum = nylon_sum + paint_sum + thinner_sum + 0.40
working_sum_per_hour = materials_total_sum * 0.3
working_sum = working_sum_per_hour * working_hours

total_sum = materials_total_sum + working_sum

print(total_sum)

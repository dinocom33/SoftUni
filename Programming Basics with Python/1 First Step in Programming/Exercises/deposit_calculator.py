deposit_sum = float(input())
deposit_time = int(input())
year_interest = float(input())

interest_per_year = deposit_sum * (year_interest / 100)
interest_per_month = interest_per_year / 12

total_sum = deposit_sum + (interest_per_month * deposit_time)

print(total_sum)

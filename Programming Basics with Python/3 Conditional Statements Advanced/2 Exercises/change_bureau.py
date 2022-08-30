bitcoin_count = int(input())
yuan_count = float(input())
commission = float(input())

total_bitcoin = bitcoin_count * 1168
total_yuan_usd = yuan_count * 0.15
yuan_to_lv = total_yuan_usd * 1.76

total_sum_lv = total_bitcoin + yuan_to_lv
total_sum_euro = total_sum_lv / 1.95
total_commission = (total_sum_euro * commission) /100

final_sum = total_sum_euro - total_commission

print(f"{final_sum:.2f}")
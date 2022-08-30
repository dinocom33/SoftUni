budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_total_sum = gpu_count * 250
cpu_total_sum = (gpu_total_sum * 0.35) * cpu_count
ram_total_sum = (gpu_total_sum * 0.10) * ram_count

total_sum = gpu_total_sum + cpu_total_sum + ram_total_sum

if gpu_count > cpu_count:
    total_sum = total_sum * 0.85
diff = abs(total_sum - budget)

if total_sum <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
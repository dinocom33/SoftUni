n = int(input())

last_pair_sum = 0
current_pair_sum = 0
diff = 0
max_diff = 0

for i in range(1, n + 1):
    first_num = int(input())
    second_num = int(input())

    if i == 1:
        last_pair_sum = first_num + second_num
    else:
        current_pair_sum = first_num + second_num
        diff = abs(current_pair_sum - last_pair_sum)
        if diff > max_diff:
            max_diff = diff
        last_pair_sum = current_pair_sum

if max_diff == 0:
    print(f"Yes, value={last_pair_sum}")
else:
    print(f"No, maxdiff={max_diff}")

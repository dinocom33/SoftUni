import sys

n = int(input())

max_number = -sys.maxsize
total_sum = 0

for i in range(0, n):
    num = int(input())
    if num > max_number:
        max_number = num
    total_sum += num

diff = abs(max_number - (total_sum - max_number))

if max_number == total_sum - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {diff}")

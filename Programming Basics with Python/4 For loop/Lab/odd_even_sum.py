n = int(input())

odd_sum = 0
even_sum = 0

for i in range(1, n + 1):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

diff = abs(even_sum - odd_sum)

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {diff}")

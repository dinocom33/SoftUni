text = input()

total_sum = 0

for i in range(0, len(text)):
    if text[i] == "a":
        total_sum += 1
    if text[i] == "e":
        total_sum += 2
    if text[i] == "i":
        total_sum += 3
    if text[i] == "o":
        total_sum += 4
    if text[i] == "u":
        total_sum += 5

print(total_sum)

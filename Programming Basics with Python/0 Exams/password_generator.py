a = int(input())
b = int(input())
max_password = int(input())

ascii_a = 35
ascii_b = 64

password_count = 0

for x in range(1, a + 1):
    for y in range(1, b + 1):
        if ascii_a > 55:
            ascii_a = 35
        if ascii_b > 96:
            ascii_b = 64
        print(f"{chr(ascii_a)}{chr(ascii_b)}{x}{y}{chr(ascii_b)}{chr(ascii_a)}|", end="")
        password_count += 1
        ascii_a += 1
        ascii_b += 1
        if password_count == max_password:
            break
    if password_count == max_password:
        break

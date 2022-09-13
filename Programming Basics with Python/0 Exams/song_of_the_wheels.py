control_number = int(input())

digits_counter = 0
password = ""

for first_digit in range(1, 10):
    for second_digit in range(1, 10):
        if first_digit < second_digit:
            for third_digit in range(1, 10):
                for forth_digit in range(1, 10):
                    if third_digit > forth_digit:
                        if (first_digit * second_digit) + (third_digit * forth_digit) == control_number:
                            digits_counter += 1
                            print(f"{first_digit}{second_digit}{third_digit}{forth_digit}", end=" ")
                            if digits_counter == 4:
                                password = f"{first_digit}{second_digit}{third_digit}{forth_digit}"
print()
if password != "":
    print(f"Password: {password}")
else:
    print("No!")

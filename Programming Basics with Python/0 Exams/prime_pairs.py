first_couple_start = int(input())
second_couple_start = int(input())
first_couple_diff = int(input())
second_couple_diff = int(input())

first_couple_end = first_couple_start + first_couple_diff
second_couple_end = second_couple_start + second_couple_diff

for current_first_couple in range(first_couple_start, first_couple_end + 1):
    for current_second_couple in range(second_couple_start, second_couple_end + 1):
        is_first_couple_prime = True
        is_second_couple_prime = True
        for first_couple in range(2, (current_first_couple // 2) + 1):
            if current_first_couple % first_couple == 0:
                is_first_couple_prime = False
                break
        for second_couple in range(2, (current_second_couple // 2) + 1):
            if current_second_couple % second_couple == 0:
                is_second_couple_prime = False
                break
        if is_first_couple_prime and is_second_couple_prime:
            print(f"{current_first_couple}{current_second_couple}")

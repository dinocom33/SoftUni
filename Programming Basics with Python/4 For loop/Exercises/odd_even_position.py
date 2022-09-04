import sys

numbers_count = int(input())

numbers = 0
odd_sum = 0
odd_min = sys.maxsize
odd_max = - sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = - sys.maxsize

for numbers in range(1, numbers_count + 1):
    current_number = float(input())
    if numbers % 2 == 0:
        even_sum += current_number
        if current_number > even_max:
            even_max = current_number
        elif current_number < even_min:
            even_min = current_number
    else:
        odd_sum += current_number
        if current_number > odd_max:
            odd_max = current_number
        elif current_number < odd_min:
            odd_min = current_number
    if odd_min == sys.maxsize:
        odd_min = odd_max
    elif odd_max == - sys.maxsize:
        odd_max = odd_min
    elif even_min == sys.maxsize:
        even_min = even_max
    elif even_max == - sys.maxsize:
        even_max = even_min

if numbers == 0:
    print(f"OddSum={odd_sum:.2f},")
    print("OddMin=No,")
    print("OddMax=No,")
    print(f"EvenSum={even_sum:.2f},")
    print("EvenMin=No,")
    print("EvenMax=No")
elif odd_sum == 0 and even_sum != 0:
    print(f"OddSum={odd_sum:.2f},")
    print("OddMin=No,")
    print("OddMax=No,")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
elif even_sum == 0 and odd_sum != 0:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print("EvenMin=No,")
    print("EvenMax=No")
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")

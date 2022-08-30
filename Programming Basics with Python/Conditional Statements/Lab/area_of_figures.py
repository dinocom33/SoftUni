from math import pi

figure_type = input()

if figure_type == "square":
    a = float(input())
    area = a * a
    print(f"{area:.3f}")
elif figure_type == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")
elif figure_type == "circle":
    r = float(input())
    area = pi * (r ** 2)
    print(f"{area:.3f}")
elif figure_type == "triangle":
    a = float(input())
    h = float(input())
    area = (a * h) / 2
    print(f"{area:.3f}")

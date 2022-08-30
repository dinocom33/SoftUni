degreeses = float(input())

if 26.00 <= degreeses <= 35.00:
    print("Hot")
elif 20.1 <= degreeses <= 25.9:
    print("Warm")
elif 15.00 <= degreeses <= 20.00:
    print("Mild")
elif 12.00 <= degreeses <= 14.9:
    print("Cool")
elif 5.00 <= degreeses <= 11.9:
    print("Cold")
else:
    print("unknown")
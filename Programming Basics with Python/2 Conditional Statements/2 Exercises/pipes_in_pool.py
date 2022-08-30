v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

first_pipe = p1 * h
second_pipe = p2 * h
total_water = first_pipe + second_pipe
percent_full = (total_water / v) * 100
percent_p1 = (first_pipe / total_water) * 100
percent_p2 = (second_pipe / total_water) * 100
diff = abs(total_water - v)

if total_water <= v:
    print(f"The pool is {percent_full:.2f}% full. Pipe 1: {percent_p1:.2f}%. Pipe 2: {percent_p2:.2f}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {diff:.2f} liters.")

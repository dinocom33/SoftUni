import math

record_in_sec = float(input())
distance_in_m = float(input())
time_per_m = float(input())

total_time_in_sec = distance_in_m * time_per_m
delay = math.floor(distance_in_m / 15) * 12.5
time_with_delay = total_time_in_sec + delay
diff = abs(time_with_delay - record_in_sec)

if time_with_delay < record_in_sec:
    print(f"Yes, he succeeded! The new world record is {time_with_delay:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")

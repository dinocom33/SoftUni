import math

serial = input()
time_serial = int(input())
time_break = int(input())

lunch_time = time_break / 8
relax_time = time_break / 4

time_left = time_break - (lunch_time + relax_time)
diff = math.ceil(abs(time_left - time_serial))

if time_left >= time_serial:
    print(f"You have enough time to watch {serial} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial}, you need {diff} more minutes.")
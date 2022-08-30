holidays = int(input())

working_days = 365 - holidays
working_day_play_time = working_days * 63
holidays_play_time = holidays * 127
total_play_time = working_day_play_time + holidays_play_time
diff = abs(30000 - total_play_time)
diff_in_hours = diff // 60
diff_in_min = diff % 60

if total_play_time < 30000:
    print("Tom sleeps well")
    print(f"{diff_in_hours} hours and {diff_in_min} minutes less for play")
else:
    print("Tom will run away")
    print(f"{diff_in_hours} hours and {diff_in_min} minutes more for play")
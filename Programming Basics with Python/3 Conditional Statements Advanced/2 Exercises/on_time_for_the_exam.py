exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time_min = (exam_hour * 60) + exam_minute
arrival_time_min = (arrival_hour * 60) + arrival_minute

diff = abs(exam_time_min - arrival_time_min)

if exam_time_min < arrival_time_min:
    print("Late")
    if diff >= 60:
        hour = diff // 60
        min = diff % 60
        print(f"{hour}:{min:02d} hours after the start")
    else:
        if diff < 60:
            print(f"{diff} minutes after the start")
elif exam_time_min == arrival_time_min or diff <= 30:
    print(f"On time")
    if diff >= 1:
        print(f"{diff} minutes before the start")
else:
    print("Early")
    if diff >= 60:
        hour = diff // 60
        min = diff % 60
        print(f"{hour}:{min:02d} hours before the start")
    else:
        print(f"{diff} minutes before the start")

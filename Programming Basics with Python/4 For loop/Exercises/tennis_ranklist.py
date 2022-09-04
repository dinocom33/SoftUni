import math

tournaments_count = int(input())
start_points = int(input())

total_points = start_points
tournament_win = 0

for i in range(1, tournaments_count + 1):
    tournament_stage = input()
    if tournament_stage == "W":
        tournament_win = tournament_win + 1
        total_points = total_points + 2000
    elif tournament_stage == "F":
        total_points = total_points + 1200
    elif tournament_stage == "SF":
        total_points = total_points + 720

avg_points = math.floor((total_points - start_points) / tournaments_count)
percentage_win = tournament_win / tournaments_count * 100

print(f"Final points: {total_points}")
print(f"Average points: {avg_points}")
print(f"{percentage_win:.2f}%")

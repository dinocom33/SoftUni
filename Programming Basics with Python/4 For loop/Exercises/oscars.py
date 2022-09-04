name = input()
academy_points = float(input())
eval_count = int(input())

total_points = academy_points

for i in range(1, eval_count + 1):
    eval_name = input()
    eval_points = float(input())
    current_points = (len(eval_name) * eval_points) / 2
    total_points = total_points + current_points

    if total_points > 1250.50:
        break

diff = abs(1250.50 - total_points)

if total_points < 1250.50:
    print(f"Sorry, {name} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {name} got a nominee for leading role with {total_points:.1f}!")

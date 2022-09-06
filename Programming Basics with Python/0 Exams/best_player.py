player_name = input()

hattrick_scored = False
most_goals_scored = 0
best_player_name = ""

while player_name != "END":
    goals_scored = int(input())
    game_goals_scored = goals_scored
    if goals_scored >= 3:
        hattrick_scored = True
    if game_goals_scored > most_goals_scored:
        most_goals_scored = game_goals_scored
        best_player_name = player_name
    if goals_scored >= 10:
        break
    player_name = input()

print(f"{best_player_name} is the best player!")
if hattrick_scored:
    print(f"He has scored {most_goals_scored} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals_scored} goals.")

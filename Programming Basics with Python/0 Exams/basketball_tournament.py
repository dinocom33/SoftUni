tournament_name = input()

total_games_count = 0
wins_count = 0
loss_count = 0

while tournament_name != "End of tournaments":
    game_count = int(input())
    for current_game in range(1, game_count + 1):
        home_tim_points = int(input())
        guest_tim_points = int(input())
        total_games_count += 1
        if home_tim_points > guest_tim_points:
            wins_count += 1
            diff = home_tim_points - guest_tim_points
            print(f"Game {current_game} of tournament {tournament_name}: win with {diff} points.")
        else:
            loss_count += 1
            diff = guest_tim_points - home_tim_points
            print(f"Game {current_game} of tournament {tournament_name}: lost with {diff} points.")

    tournament_name = input()
percent_wins = wins_count / total_games_count * 100
percent_losses = loss_count / total_games_count * 100

print(f"{percent_wins:.2f}% matches win")
print(f"{percent_losses:.2f}% matches lost")

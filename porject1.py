import random

def roll():
    min = 1
    max = 15
    roll = random.randint(min, max)

    return roll
while True:
    players = input("Enter the number of players(1-4): ")
    if players.isdigit():
        players = int (players)
        if players >= 1 and players <= 4:
            break
        else:
            print("Must be between 1 and 4")
    else:
        print("Invalid input")
max_score = 100
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for player_index in range(players):
        print("Player", player_index + 1, "turn\n")
        print("your total score is", players_scores[player_index])
        current_score = 0

        while True:
            should_roll = input("would you like to roll? (y): ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1. Your turn is over.")
                curent_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)

            print("Your score is", current_score)
        players_scores[player_index] = current_score
        print('your total score is', players_scores[player_index])
    
max_score = (max(players_scores))
winner = players_scores.index(max_score)
print("The winner is player", winner + 1, "with a score of", max_score)
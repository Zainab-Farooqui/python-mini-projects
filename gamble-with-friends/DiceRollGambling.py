import random

def roll():
    value = random.randint(1, 6)
    return value

no_of_player = int(input("How many players are there? "))
all_players_scores = [0 for _ in range(no_of_player)]

while max(all_players_scores) < 50:
    for i in range(no_of_player):        
        print("**************************************************************************************************\n")
        current_score = 0 
        print(f"Player {i + 1} turn:")

        while True:
            
            want_to_roll = input("Do you wanna roll the dice? (y/n): ").lower()
            if want_to_roll != 'y':
                break

            score = roll()
            if score == 1:
                print("You rolled a 1!")
                current_score = 0
                break
            else:
                current_score += score
                print(f"You rolled a {score}!")  

            print(f"Current score for this turn: {current_score}")      


        all_players_scores[i] += current_score
        print(f"Your score is {all_players_scores[i]}")
        

win = max(all_players_scores)
player_won = all_players_scores.index(win) + 1
print(f"\n\nPlayer {player_won} wins with a score of {win}!")

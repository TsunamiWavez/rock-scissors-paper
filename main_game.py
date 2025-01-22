from random import choice

# Input options
print("---ROCK---SCISSORS---PAPER---\n"
      "\nOptions of your input:"
      "\n\t1 - Rock;"
      "\n\t2 - Scissors;"
      "\n\t3 - Paper; "
      "\n\t4 - Show game statistics;"
      "\n\t5 - Quit the game."
      "\n\nPlease use only these options (from 1 to 5), "
      "\notherwise the program will return an error! ")

def get_choices():
    """Function for getting the results of user and computer choices"""
    player_choice_number = input("\nEnter your choice (rock, scissors, paper):"
                                 "\n>>> ")
    try:
        player_choice_number = int(player_choice_number)
    except ValueError:
        player_choice_number = None

    player_options = {1: "rock", 2: "scissors", 3: "paper",
                      4: "statistics", 5: "exit"
                      }
    computer_options = ["rock", "scissors", "paper"]

    computer_choice = choice(computer_options)

    try:
        player_choice = player_options[player_choice_number]
    except KeyError:
        player_choice = None

    choices = {'player': player_choice,
               'computer': computer_choice,
               }

    return choices


def get_result(player, computer):
    """Function for getting the results of the game"""
    if player == computer:
        return "Draw!"
    elif player == 'rock':
        if computer == 'scissors':
            return"You won! :D"
        else:
            return "You lost :("
    elif player == 'scissors':
        if computer == 'paper':
            return"You won! :D"
        else:
            return "You lost :("
    elif player == 'paper':
        if computer == 'rock':
            return"You won! :D"
        else:
            return "You lost :("
    elif player == 'exit':
        return 'exit'
    elif player == 'statistics':
        return 'statistics'
    else:
        return None


game_active = True

player_wins = 0
computer_wins = 0
tie_number = 0

while game_active:
    choices = get_choices()
    result = get_result(choices['player'], choices['computer'])

    if result == 'exit':
        print('\nThe game is over...')
        game_active = False
        break
    elif result is None:
        print("\nThere was an error. Please enter the input data correctly!")
    elif result == 'statistics':
        print(f"\nYour wins: {player_wins}")
        print(f"Computer's wins: {computer_wins}")
        print(f"Ties: {tie_number}")
    else:
        print(f"\nYou chose {choices['player']}."
              f"\nComputer chose {choices['computer']}.")
        print(f'\n{result}')
        if "won" in result:
            player_wins += 1
        if "lost" in result:
            computer_wins += 1
        if "draw" in result.lower():
            tie_number += 1

# Rock Scissors Paper - Console Game

This is a simple console-based implementation of the classic "Rock, Scissors, Paper" game, where you can play against a computer opponent. 
The game provides a user-friendly interface for making selections and keeps track of the game statistics.

## Features
- Play "Rock, Scissors, Paper" against the computer.
- View game statistics including the number of wins, losses, and ties.
- Option to quit the game at any time.

## How to Play
1. Run the program.
2. Enter your choice by selecting a number from the given options:
   - `1` for Rock
   - `2` for Scissors
   - `3` for Paper
   - `4` to show game statistics
   - `5` to quit the game
3. The computer will make its choice randomly.
4. The result of the game (win, lose, or draw) will be displayed.
5. You can continue playing or choose to view the statistics or exit the game.

## Game Rules
- **Rock** beats **Scissors**
- **Scissors** beats **Paper**
- **Paper** beats **Rock**
- If both choices are the same, it's a **draw**.

## Example Output
```
---ROCK---SCISSORS---PAPER---

Options of your input:
	1 - Rock;
	2 - Scissors;
	3 - Paper;
	4 - Show game statistics;
	5 - Quit the game.

Please use only these options (from 1 to 5), otherwise the program will return an error!

Enter your choice (rock, scissors, paper):
>>> 1

You chose rock.
Computer chose paper.

You lost :(

Enter your choice (rock, scissors, paper):
>>> 4

Your wins: 0
Computer's wins: 1
Ties: 0
```

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.



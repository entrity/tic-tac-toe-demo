# Tic-tac-toe

Go head to head against the computer in a game of tic-tac-toe (a.k.a. 'noughts and crosses').

## Playing the game

Run the main script with Python 3. (It was developed with Python 3.6.8.) 

```bash
python3 main.py
# Or if `env` is working on your system and you prefer:
./main.py
```

No non-core libraries are required.

### Dynamics of the game.

The terminal will prompt you for which player you wish to be (X or O). X always plays first. The computer will play with whichever token you did not choose.

At each of your turns, the terminal will display the current state of the game and then prompt you for a cell in the grid which you wish to claim. You can see in the display on the terminal that the columns and rows of the game board are encoded with the letters A, B, C and the numbers 1, 2, 3:

```
    A   B   C
  +---+---+---+
1 |   |   |   |
  +---+---+---+
2 |   |   |   |
  +---+---+---+
3 |   |   |   |
  +---+---+---+
```

Enter your move as a two-character identifier, staring with the letter and finishing with the numeral. (This game is *not* case sensitive.)

## The AI

Because the search space for a game of tic-tac-toe is so small, I saved a bit of programming time by implementing the minimax algorithm without alpha-beta pruning or restrictions on search depth. The lack of pruning imposes a computational cost that can impose a wait on older machines, but I did not find that this inhibited gameplay on my development machine.

If you think the performance merits the extra dev time, you can modify the minimax implementation to include pruning in the `game_tree.py` file. For much less investment, you can modify the `_minimax_recursive` function in the `game_tree.py` file to support a limit on the search depth. (If you do the latter, be sure to call the `calc_score` function because you will definitely need to evaluate some non-terminal game states.)

## Running the automated tests

There are a couple of test scripts whose names are prefixed with `test_`, which contain unit tests to aid in development. See the comments in each file for instructions on using them.

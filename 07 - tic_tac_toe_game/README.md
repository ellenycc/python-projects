# Tic-Tac-Toe

## Goal

Create a classic Tic Tac Toe game where two players take turns marking Xs and Os on a 3x3 grid. The first player to align three of their marks vertically, horizontally, or diagonally wins. The board updates after each move, with colored marks to distinguish between players. The game checks for a winner after each move and ends when a player wins or the board is full, resulting in a draw.

## Key Takeaways

1. **Define the Data Structure**: Break down the game into small steps and write pseudocode to establish a clear structure.

2. **Use of For Loop**: Iterate over each row and column to check for three aligned marks horizontally or vertically.

3. **Python Package - termcolor**: Enhance the game's visual appeal by using the `termcolor` package to assign different colors to each player's moves.

  ```python
  from termcolor import colored

  def switch_color(current_player):
    color = 'red' if current_player == 'X' else 'green'
    return colored(current_player, color)

  def get_move(current_player):
    while True:
      # snip: code to get row and column input
      if board[row][column] == " ":
        board[row][column] = switch_color(current_player)
        break
      print("This spot is already taken")
  ```


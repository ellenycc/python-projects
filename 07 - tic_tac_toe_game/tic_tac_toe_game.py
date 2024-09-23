from termcolor import colored

X = "X"
O = "O"

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def display_board(board):
    line = "---+---+---"
    print(line)
    for row in board:
        print(f" {row[0]} | {row[1]} | {row[2]}")
        print(line)


def check_winner(board):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # check columns
    for column in range(3):  # [0, 1, 2]
        if board[0][column] == board[1][column] == board[2][column] != " ":
            return True

        # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " " or \
            board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def is_board_complete(board):
    for row in board:
        if " " in row:
            return False

    return True


def get_position(prompt):
    while True:
        try:
            # check if the input can be converted to integer
            position = int(input(prompt))
            if position < 0 or position > 2:
                raise ValueError()
            return position
        except ValueError:
            print("Invalid input")


def switch_color(current_player):
    color = 'red' if current_player == X else 'green'
    return colored(current_player, color)


def get_move(current_player):
    print(f"Player {current_player}'s turn")
    while True:
        row = get_position("Enter row (0-2): ")
        column = get_position("Enter column (0-2): ")

        if board[row][column] == " ":
            board[row][column] = switch_color(current_player)
            break

        print("This spot is already taken")


def main():
    display_board(board)

    current_player = X
    while True:
        get_move(current_player)

        display_board(board)

        if check_winner(board):
            print(f"Player {current_player} wins!")
            break

        if is_board_complete(board):
            print(f"Game over")
            break

        current_player = O if current_player == X else X


if __name__ == "__main__":
    main()

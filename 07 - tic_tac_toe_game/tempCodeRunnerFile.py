        if is_board_complete(board):
            print(f"Game over")
            break

        current_player = "O" if current_player == "X" else "X"
import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 13)

# Function to check if a player has won
def is_winner(board, player):
    # Check each row
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check each column
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    # If none of the above conditions are met, the player has not won
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to get user move
def get_user_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to calculate computer move
def calculate_computer_move(board, player_symbol, computer_symbol):
    magic_square = [
        [8, 3, 4],
        [1, 5, 9],
        [6, 7, 2]
    ]

    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

    # Check if the computer can win in the next move
    for i, j in empty_cells:
        temp_board = [row[:] for row in board]
        temp_board[i][j] = computer_symbol
        if is_winner(temp_board, computer_symbol):
            return i * 3 + j + 1

    # Check if the opponent can win in the next move, block them
    for i, j in empty_cells:
        temp_board = [row[:] for row in board]
        temp_board[i][j] = player_symbol
        if is_winner(temp_board, player_symbol):
            return i * 3 + j + 1

    # If no winning move or blocking move is possible, choose a random empty cell
    return random.choice(empty_cells)[0] * 3 + random.choice(empty_cells)[1] + 1

# Function to play Tic-Tac-Toe
def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    user_symbol, computer_symbol = 'X', 'O'

    print("Welcome to Tic-Tac-Toe using Magic Square technique!")
    print_board(board)

    for move_num in range(1, 10):
        # Determine current player
        current_player = user_symbol if move_num % 2 == 1 else computer_symbol

        # Get move from current player
        if current_player == user_symbol:
            user_move = get_user_move()
            row, col = divmod(user_move - 1, 3)
        else:
            computer_move = calculate_computer_move(board, user_symbol, computer_symbol)
            row, col = divmod(computer_move - 1, 3)
            print(f"Computer chooses position {computer_move}")

        # Check if the chosen cell is empty
        while board[row][col] != ' ':
            print("ERROR! That position is already taken. Choose a different one.")
            if current_player == user_symbol:
                user_move = get_user_move()
                row, col = divmod(user_move - 1, 3)
            else:
                computer_move = calculate_computer_move(board, user_symbol, computer_symbol)
                row, col = divmod(computer_move - 1, 3)

        # Update the board with the current player's symbol
        board[row][col] = user_symbol if current_player == user_symbol else computer_symbol
        print_board(board)

        # Check for a winner
        if is_winner(board, current_player):
            print(f"{current_player} wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print("It's a tie!")
            break

# Start the game
play_tic_tac_toe()

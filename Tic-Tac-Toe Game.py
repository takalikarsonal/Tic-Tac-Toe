import random

# Function to print the board
def print_board(board):
    print("\n")
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("-" * 5)
    print("\n")

# Function to check if the current player has won
def check_win(board, player):
    for row in range(3):
        if all([spot == player for spot in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full
def check_draw(board):
    return all([board[row][col] != " " for row in range(3) for col in range(3)])

# Function for computer to make a random move
def computer_move(board):
    empty_spots = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    return random.choice(empty_spots)

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Create empty 3x3 board
    current_player = "X"  # Player X starts (player is X, computer is O)

    while True:
        print_board(board)
        
        if current_player == "X":  # Player's turn
            print("Your turn!")
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] != " ":
                    print("This spot is already taken, try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input, please enter values between 0 and 2 for row and column.")
                continue
            board[row][col] = current_player
        else:  # Computer's turn
            print("Computer's turn!")
            row, col = computer_move(board)
            board[row][col] = current_player
            print(f"Computer chooses row {row} and column {col}")

        # Check for win or draw
        if check_win(board, current_player):
            print_board(board)
            if current_player == "X":
                print("You win!")
            else:
                print("Computer wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()

import math

board = [" " for _ in range(9)]


def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def board_full():
    return " " not in board


def minimax(is_maximizing):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def ai_move():
    best_score = -math.inf
    best_position = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_position = i

    board[best_position] = "O"


print("TIC-TAC-TOE AI")
print("You are X")
print("AI is O")

while True:
    display_board()

    try:
        position = int(input("Enter position (1-9): ")) - 1

        if position < 0 or position > 8:
            print("Please enter a number from 1 to 9.")
            continue

        if board[position] != " ":
            print("Position already occupied.")
            continue

        board[position] = "X"

    except ValueError:
        print("Please enter a valid number.")
        continue

    if check_winner("X"):
        display_board()
        print("You win!")
        break

    if board_full():
        display_board()
        print("It's a draw!")
        break

    ai_move()

    if check_winner("O"):
        display_board()
        print("AI wins!")
        break

    if board_full():
        display_board()
        print("It's a draw!")
        break

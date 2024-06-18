import random

def display_board(board):
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print("|   " + "   |   ".join(str(cell) for cell in row) + "   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Please enter a number between 1 and 9.")
            else:
                row, col = divmod(move - 1, 3)
                if board[row][col] in ['O', 'X']:
                    print("Square already taken. Choose another one.")
                else:
                    board[row][col] = 'O'
                    break
        except ValueError:
            print("Invalid input. Please enter a number.")

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        if all(board[row][col] == sign for row, col in condition):
            return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'

def tic_tac_toe():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    board[1][1] = 'X'
    
    while True:
        display_board(board)
        if victory_for(board, 'X'):
            print("Machine wins!")
            break
        elif victory_for(board, 'O'):
            print("You win!")
            break
        elif not make_list_of_free_fields(board):
            print("It's a tie!")
            break
        
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("You win!")
            break
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)
            print("Machine wins!")
            break
        elif not make_list_of_free_fields(board):
            display_board(board)
            print("It's a tie!")
            break

tic_tac_toe()

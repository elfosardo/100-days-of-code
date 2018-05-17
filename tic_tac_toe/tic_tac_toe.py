import random

PLAYER = 'player'
COMPUTER = 'computer'


def make_board():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    return board


def print_board(board):
    for line in board:
        print('|'.join(line))
    return None


def get_player_move(board):
    space_taken = True
    while space_taken:
        player_move = []
        x = check_value('Column value (1-3): ')
        y = check_value('Row value (1-3): ')
        real_x = x - 1
        real_y = y - 1
        if board[real_x][real_y] is not ' ':
            print('Space already taken, choose again!')
        else:
            space_taken = False
    player_move.extend([real_x, real_y])
    return player_move


def check_value(message):
    incorrect_value = True
    while incorrect_value:
        str_number = input(message)
        number = int(str_number)
        if number not in range(1, 4):
            print('Value must be between 1 and 3')
        else:
            incorrect_value = False
    return number


def get_computer_move(board):
    computer_move = [2, 2]
    return computer_move


def check_for_winner(board):
    return False


if __name__ == '__main__':

    print('Welcome to Tic-Tac-Toe!')

    player_team = input('Do you want to be X or O?\n').upper()

    if player_team == 'X':
        computer_team = 'O'
    else:
        computer_team = 'X'

    whose_turn = random.choice([PLAYER, COMPUTER])
    print('The {} will go first.'.format(whose_turn))

    board = make_board()

    while True:
        if whose_turn == PLAYER:
            print_board(board)
            x, y = get_player_move(board)
            board[x][y] = player_team

        else:
            x, y = get_computer_move(board)
            board[x][y] = computer_team

        winner = check_for_winner(board)
        if winner:
            print('-------------------')

            if winner == 'tie':
                print("It's a tie!")
            else:
                print('The {} wins!'.format(whose_turn))

            print_board(board)
            break

        if whose_turn == PLAYER:
            whose_turn = COMPUTER
        else:
            whose_turn = PLAYER

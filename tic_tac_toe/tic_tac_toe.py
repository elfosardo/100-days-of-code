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
        print(' | '.join(line))
    return None


def get_player_move(board):
    space_taken = True
    player_move = []
    real_x = None
    real_y = None
    while space_taken:
        x = check_value('Row value (1-3): ')
        y = check_value('Column value (1-3): ')
        real_x = x - 1
        real_y = y - 1
        space_selected = board[real_x][real_y]
        space_taken = check_space_taken(space_selected)
        if space_taken:
            print('Space already taken, choose again!')
    player_move.extend([real_x, real_y])
    return player_move


def check_value(message):
    incorrect_value = True
    number = None
    while incorrect_value:
        str_number = input(message)
        number = int(str_number)
        if number not in range(1, 4):
            print('Value must be between 1 and 3')
        else:
            incorrect_value = False
    return number


def check_space_taken(space_selected):
    if space_selected is not ' ':
        return True
    return False


def get_computer_move(board):
    space_taken = True
    computer_move = []
    while space_taken:
        real_x = random.randint(0, 2)
        real_y = random.randint(0, 2)
        space_selected = board[real_x][real_y]
        space_taken = check_space_taken(space_selected)
        if not space_taken:
            computer_move = [real_x, real_y]
    return computer_move


def check_for_winner(board):
    victory_lines = [
        [board[0][0], board[0][1], board[0][2]],  # row1
        [board[1][0], board[1][1], board[1][2]],  # row2
        [board[2][0], board[2][1], board[2][2]],  # row3
        [board[0][0], board[1][0], board[2][0]],  # column1
        [board[0][1], board[1][1], board[2][1]],  # column2
        [board[0][2], board[1][2], board[2][2]],  # column3
        [board[0][0], board[1][1], board[2][2]],  # diag1
        [board[2][0], board[1][1], board[0][2]]  # diag2
    ]
    for line in victory_lines:
        if ' ' not in line:
            if line.count(line[0]) == len(line):
                return line[0]
    if ' ' not in board[0] and \
        ' ' not in board[1] and \
            ' ' not in board[2]:
        return 'tie'
    return False


if __name__ == '__main__':

    print('Welcome to Tic-Tac-Toe!')

    player_team = ''
    choices = ['x', 'X', 'y', 'Y']
    while player_team not in choices:
        player_team = input('Do you want to be X or O?\n').upper()
        print(player_team)
        if player_team not in choices:
            print('must choose X or Y')

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

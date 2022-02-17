import random

X = "X"
O = "O"
EMPTY = "*"
# this is daniel commmit
# Bigger board sizes are less likely
RANDOM_SIZES = [3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]

# Type aliases
Player = str
Board = list[list]
Coords = tuple[int, int]


def create_board(size: int) -> Board:
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(EMPTY)
        board.append(row)
    return board


def check_rows(board, player):
    for row in board:
        if row.count(player) == len(row):
            return True
    return False


def check_columns(board, player):
    for i, row in enumerate(board):
        marks = 0
        for j in range(len(row)):
            marks += board[j][i] == player
        if marks == len(row):
            return True
    return False


def check_diagonals(board, player):

    marks = 0
    marks_sec = 0
    for i, row in enumerate(board):
        marks += board[i][i] == player
        marks_sec += board[i][len(row)-1 - i] == player
    if marks == len(row) or marks_sec == len(row):
        return True
    return False



def won(player: Player, board: Board) -> bool:
    return check_rows(board, player) or check_columns(board, player) or check_diagonals(board, player)


def update_board(board: Board, player: Player, coords: Coords):
    if board[coords[0]][coords[1]] != EMPTY:
        print("this is a used square! try again")
        return False
    else:
        board[coords[0]][coords[1]] = player
        return True



def get_move(player: Player) -> Coords:
    row, col = input(f"{player}'s move: ").split()
    return int(row), int(col)


def show_board(board: Board):
    for row in board:
        print(" ".join(row))


def show_winner(player: Player):
    print(f"\nAnd the WINNER is: .....\n!!!!!!!!!!!! {player} !!!!!!!!!!!!")


def switch_player(current_player: Player) -> Player:
    return X if current_player == O else O


def play_game(board_size: int = None):
    if not board_size:
        board_size = random.choice(RANDOM_SIZES)
    board = create_board(board_size)
    current_player = X
    while not won(current_player, board):
        show_board(board)
        coordinates = get_move(current_player)
        check_update = update_board(board, current_player, coordinates)
        if check_update:
            current_player = switch_player(current_player)
    show_winner(current_player)


if __name__ == '__main__':
    play_game(3)

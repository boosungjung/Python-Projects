board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


def drawBoard(player=0, row=0, column=0):
    print("   0  1  2")
    board[row][column] = player
    for column, row in enumerate(board):
        print(column, row)


def winner():
    global play
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Winner!")
            play = False

    column = []
    for col in board:
        column.append(col[0])
    if column.count(column[0]) == len(column) and column[0] != 0:
        print("Winner!")
        play = False

    diag = []
    for xi in range(len(board)):
        diag.append(board[xi][xi])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
        print("Winner!")
        play = False

    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(board)))):
        diags.append(board[idx][reverse_idx])

    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print("Winner!")
        play = False


play = True
winner()
while play:
    winner()
    drawBoard()
    #player 1
    row1 = int(input("Player 1: Choose row position"))
    column1 = int(input("Player 1: Choose column position"))
    drawBoard(player='x', row=row1, column=column1)
    winner()

    #player 2
    row2 = int(input("Player 2: Choose row position"))
    column2 = int(input("Player 2: Choose column position"))
    drawBoard(player='y', row=row2, column=column2)
    winner()



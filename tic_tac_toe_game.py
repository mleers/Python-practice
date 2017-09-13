def contestant(mark):
    if mark == 'X':
        return('Player1')
    elif mark == 'O':
        return('Player2')

def gameboard():
    board = [[' ---', ' ---', ' ---'],
             ['|   ', '|   ', '|   ', '|   '],
             [' ---', ' ---', ' ---'],
             ['|   ', '|   ', '|   ', '|   '],
             [' ---', ' ---', ' ---'],
             ['|   ', '|   ', '|   ', '|   '],
             [' ---', ' ---', ' ---']]
    return(board)

def make_gameboard(board):
    for line in board:
        print(''.join(line))

def play(board, player, mark):
    player = input('%s [row col]: ' %(player))
    while True:
        row = int(player.split()[0])
        col = int(player.split()[1]) - 1
        trans_row = {1:1, 2:3, 3:5}
        if row in range(1, 4) and col in range(0, 3):
            if board[trans_row[row]][col] == '|   ':
                board[trans_row[row]][col] = '| %s ' %(mark)
                make_gameboard(board)
                break
            else:
                print('Space already chosen')
                player = input('Please repick')
        else:
            print('Incorrect input')
            player = input('Please repick')

def win(board):
    for i in range(1, 6, 2): # Checks row win conditions
        row = set([board[i][0], board[i][1], board[i][2]])
        if len(row) == 1 and board[i][0] != '|   ':
            return('The winner is %s!' %(contestant(board[i][0][2])))

    for j in range(3): # Checks column win conditions
        column = set([board[1][j], board[3][j], board[5][j]])
        if len(column) == 1 and board[1][j] != '|   ':
            return('The winner is %s!' %(contestant(board[1][j][2])))

    # Checks diagonal win conditions
    if board[1][0] == board[3][1] == board[5][2] and board[3][1] != '|   ':
        return('The winner is %s!' %(contestant(board[3][1][2])))
    elif board[1][2] == board[3][1] == board[5][0] and board[3][1] != '|   ':
        return('The winner is %s!' %(contestant(board[3][1][2])))

    else:
        return(0)



board = gameboard()
player1, mark1 = 'Player1', 'X'
player2, mark2 = 'Player2', 'O'

done = False
while not done:
    play(board, player1, mark1)
    if win(board) == 0:
        play(board, player2, mark2)
        done = False
    else:
        print(win(board))
        done = True

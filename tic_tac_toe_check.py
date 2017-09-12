board1 = [[2,2,0], [2,1,0], [2,1,1]]
board2 = [[1,2,0], [2,1,0], [2,1,1]]
board3 = [[0,1,0], [2,1,0], [2,1,1]]
board4 = [[1,2,0], [2,1,0], [2,1,2]]
board5 = [[1,2,0], [2,1,0], [2,1,0]]

def tttcheck(matrix):
	for x in range(0,3):
		row = set([matrix[x][0], matrix[x][1], matrix[x][2]])
		if len(row) == 1 and matrix[x][0] != 0:
			return matrix[x][0]

	for x in range(0,3):
		col = set([matrix[0][x], matrix[1][x], matrix[2][x]])
		if len(col) == 1 and matrix[0][x] != 0:
			return matrix[0][x]

	diagleft = set([matrix[0][0], matrix[1][1], matrix[2][2]])
	diagright = set([matrix[0][2], matrix[1][1], matrix[2][0]])
	if len(diagleft) == 1 or len(diagright) == 1 and matrix[1][1] != 0:
		return matrix[1][1]

	return 0


print(tttcheck(board3))

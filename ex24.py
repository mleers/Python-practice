print("Welcome to the board game grid creator")
x = int(input("Type number(s) of columns: "))
y = int(input("Type number(s) of rows: "))

def asker(x,y):
	col = []
	row = []

	for i in range(x):
		col.append("|   |")
	for i in range(x):
		row.append(" --- ")	
	for i in range(y):
		print("".join(row))
		print("".join(col))
		print("".join(row))
	
	return x,y
asker(x,y)


def maxxer(input1, input2, input3):

	biggest = 0

	if input1 > input2 and input1 > input3:
		biggest = input1
	elif input2 > input1 and input2 > input3:
		biggest = input2
	elif input3 > input2 and input3 > input1:
		biggest = input3
	else:
		print("Largest occurs more than once")
	return biggest


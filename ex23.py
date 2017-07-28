def filecomp(filename):
	returner_list = []
	with open(filename) as f:
		line = f.readline()
		while line:
			returner_list.append(int(line))
			line = f.readline()
	return returner_list

list_1 = input('Enter the first file to compare: ')
list_2 = input('Enter the second file to compare: ')

file_1 = filecomp(list_1)
file_2 = filecomp(list_2)

shared = [i for i in file_1 if i in file_2]

print("The shared elements are: ")
print(shared)



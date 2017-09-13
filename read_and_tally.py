# Uses names from http://www.practicepython.org/assets/Training_01.txt

names = {}
with open('namefile.txt') as f:
	line = f.readline()
	while line:
		line = line[3:-26]
		if line in names:
			names[line] += 1
		else:
			names[line] = 1
		line = f.readline()
	
print(names)	

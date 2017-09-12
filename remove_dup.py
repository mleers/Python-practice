def dupcheck(a):
	new_list = []
	for i in a:
		if i not in new_list:
			new_list.append(i)
	return new_list
	
#2nd method

def dupcheck1():

        return list(set(a))


a = input("Insert a list with a duplicate(s): ")

print "Using loops: ", dupcheck(a)
print "Using set: ", dupcheck1()


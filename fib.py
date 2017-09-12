n = int(input("Input how many numbers of the fibonnaci sequence to print: "))

def fibber(n):
	f = []
	if n == 0 or n == 1:
		f.append(n)
	elif n == 2:
		f = [1,1]
	elif n > 2:
		f = [1,1]
		for i in range(n-2):
			z = f[-1] + f[-2]
			f.append(z)
	return(f)
print fibber(n)

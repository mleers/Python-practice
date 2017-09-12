num = int(input("Enter a number to see if it is prime: "))

a = [x for x  in range(2, num) if num % x == 0]

def primer(n):
	if num > 1:
		if len(a) == 0:
			print("Is a prime number")
		else:
			print("Not a prime number")
	else:
		print("Not a prime number")

primer(num)	

num = int(input("Enter a number to find its divisors: "))

range = list(range(1,num+1))

divisorList = []

for i in range:
	if num % i == 0:
		divisorList.append(i)

print divisorList 


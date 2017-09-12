import random

lower = 0
upper = 101
count = 0
response = ""
cpu_guess = random.randint(lower,upper)

print("Think of a number from 0 - 100 for the cpu to guess")
response = input("Do you have a number in mind? (y/n)")

if response == 'n':
	quit()

elif response == 'y':

	while True:
		count += 1

		print("The cpu picks: {}.".format(cpu_guess))
		response = input()
		if response == "higher":
			lower = cpu_guess + 1
			cpu_guess = random.randint(lower,upper)
		elif response == "lower":
			upper = cpu_guess - 1
			cpu_guess = random.randint(lower,upper)
		elif response == "yes":
			print("I am so smart, it took me {} guesses.".format(count))
			break
		else:
			print("You need to enter higher/lower/yes as a response.")


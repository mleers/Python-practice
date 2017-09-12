#A cow is a correct number in the correct place, a bull is a correct number in the wrong place

import random
num = str(random.randint(1000, 10000))

def game():
	num_guess = raw_input("Guess the number: ")
	Bulls, Cows, count  = 0,0,1
	while num_guess != num:
		count += 1
		for i in range(len(num_guess)):
			if num_guess[i] == num[i]:
				Cows += 1
			elif num_guess[i] in num:
				Bulls += 1
		print("%s Cows, %s Bulls") % (Cows, Bulls)
		num_guess  = raw_input("Guess again: ")
		Bulls,Cows = 0,0
	else:
		print("You figured out the number was %s in %s guesses!") % (num, count)



if __name__ == "__main__":
		print("Welcome to Cows and Bulls")
		start = raw_input("Do you want to play? (y/n)")
		while start != "y" and start != "n":
			start = raw_input("You must pick (y/n)")
		if start == "y":
			game()
		elif start == "n":
			quit()





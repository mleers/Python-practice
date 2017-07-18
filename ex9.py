import random

num = random.randint(1,9)
count = 0
user_guess = 0

while user_guess != num and user_guess != "exit":
	user_guess = input("Guess which number from 1-9 inclusive that I'm thinking of: ")	

	if user_guess == "exit":
		break

	count += 1	

	if user_guess > num:
		print("Too high, guess again!")
		
	elif user_guess < num:
		print("Too low, guess again!")

	else:
                print("That's the number!")
                print("It took you %s tries") % (count)


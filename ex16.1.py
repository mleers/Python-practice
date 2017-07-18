import random
import string

strength = int(raw_input("How many characters long would you like your password to be?: "))

def gen():

	let = random.choice(string.ascii_letters)
	num = random.choice(string.digits)
	sym = random.choice(string.punctuation)

gen()

def maker():
	passw = []
	gens = string.ascii_letters + string.digits + string.punctuation
	
	passw = ''.join(random.sample(gens, strength))
		
	print("Your password is: "), passw

maker()

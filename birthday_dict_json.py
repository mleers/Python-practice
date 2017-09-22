import json
birthday = {}

with open("birthday_list.json", "r") as f:    #json file made externally in python
	birthday = json.load(f)

print("Welcome to the birthday selector.  Birthdays of the following people are known: ")
for x in birthday:
	print(x)

choice= input("Who's birthday do you want to look up?").title()

if choice in birthday:
	print("The birthday of {} is {} ".format(choice, birthday[choice]))
elif choice not in birthday:
	not_found = input("Name not found.  Add name to list? (y/n)").upper()
	if not_found == 'N':
		quit()
	elif not_found == 'Y':
		add_date = input("Enter birthdate: ")
		birthday[choice] = add_date
		with open("birthday_list.json", "w") as f:
			json.dump(birthday, f)
		print("{} was added to the birthday list with birthday of {}".format(choice, add_date))


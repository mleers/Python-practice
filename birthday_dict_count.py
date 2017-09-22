import json
from collections import Counter

birthday = {}
months = []

with open("birthday_list.json", "r") as f:    #json file made externally in python
	birthday = json.load(f)

month_to_name = {
	1: "January",
	2: "February",
	3: "March",
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}


for name, birthdays in birthday.items():
	month = int(birthdays.split("/")[0])
	months.append(month_to_name[month])

print("Welcome to the birthday selector.  Birthdays of the following people are known: ")
for x in birthday:
	print(x)
print("The amount of birthdays per month so far is as follows: ")
print(Counter(months))

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


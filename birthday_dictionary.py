birthdays ={
	"Albert Einstein": "3/14/1889",
	"Bill Gates": "10/28/1955",
	"George Washington": "2/22/1732",
	"b": "1/1/2001"
}

print("Welcome to the birthday selector.  Birthdays of the following people are known: ")
for x in birthdays:
    print(x)

choice= input("Who's birthday do you want to look up?")

if choice in birthdays:
    print("The birthday of {} is {} ".format(choice, birthdays[choice]))

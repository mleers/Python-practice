import datetime
today_year = datetime.date.today().year
current_year = int(today_year)

name = raw_input("Enter your name: ")
age = raw_input("Enter your age: ")

print "Your name is: ", name
print "Your age is: ", age

year = 100 - int(age)
year_100 = int(current_year) + year
statement = "You will turn 100 in %s years in %s" % (year, year_100)

print "You will turn 100 in %s years in %s" % (year, year_100)


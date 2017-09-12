import random

a = random.sample(range(100), 10)

print "The list is: ", sorted(a)

even_a = [num for num in a if num % 2 == 0]
odd_a = [num for num in a if num % 2 != 0]

print "The even numbers in the list are: ", sorted(even_a)
print "The odd numbers in the list are: ", sorted(odd_a)




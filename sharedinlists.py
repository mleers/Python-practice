import random

list1 = random.sample(range(1,20), 9)
list2 = random.sample(range(1,20), 14)

print "List one is: ",list1
print "List two is: ",list2

shared_nums = []

for num in list1:
	if num in list2:
		shared_nums.append(num)


print "The shared numbers between the two lists are: ",shared_nums


	

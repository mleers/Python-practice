import random

list1 = sorted(random.sample(range(1,20), 9))
list2 = sorted(random.sample(range(1,20), 14))

print "List one is: ", list1
print "List two is: ", list2

shared_nums = []
shared_nums = [num for num in list1 and list2 if num in list1 and num in list2]	

print "The shared numbers in each list are: ", shared_nums


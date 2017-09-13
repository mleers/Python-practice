import random

#uses text file from http://norvig.com/ngrams/sowpods.txt

with open('sowpods.txt', encoding = 'utf-8') as a_file:
	lines = a_file.readlines()

print(random.choice(lines).strip())

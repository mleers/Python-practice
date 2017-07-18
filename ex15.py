def str_rev():

	string = input("Type a sentence: ")

	sp_str = string.split()

	sp_str1 = sp_str[::-1]

	sp_str2 = " ".join(sp_str1)
	
	print "Your reversed sentence is: ",  sp_str2

str_rev()


print "Welcome to rock paper scissors.  Play someone for best of 3"

def player_1():
	x = raw_input('Player 1 pick "rock" "paper" or "scissors": ')
	while x != "rock" and x != "paper" and x != "scissors":
		x = raw_input('You must pick "rock" "paper" or "scissors"')
	return x

def player_2():
	x = raw_input('Player 2 pick "rock" "paper" or "scissors": ')
	while x != "rock" and x != "paper" and x != "scissors":
		x = raw_input('You must pick "rock" "paper" or "scissors"')
        return x		

def retry():
	retry = raw_input('Would you like to play again? Pick "yes" or "no"')
	while retry != "yes" and retry != "no":
		retry = raw_input('Pick "yes" or "no"')
        if retry == "yes":
		return scorer()
        elif retry == "no":
		print "Goodbye"
 
def scorer():
	Score1 = 2
	Score2 = 2
	while Score1 > 0 and Score2 >0:
		P1 = player_1()
		P2 = player_2()
		if P1.lower() == P2.lower():
			print "it's a tie!"
		elif P1.lower() == "rock" and P2.lower() == "scissors":
			print "Player 1 Wins!"
			Score1 -= 1
			print "Player 1 has score of: ", Score1
			print "Player 2 has score of: ", Score2
		elif P1.lower() == "paper" and P2.lower() == "rock":
		       	print "Player 1 Wins!"
	   	   	Score1 -= 1
			print "Player 1 has score of: ", Score1
        	        print "Player 2 has score of: ", Score2
		elif P1.lower() == "scissors" and P2.lower() == "paper":
		    	print "Player 1 Wins!"
		    	Score1 -= 1
			print "Player 1 has score of: ", Score1
			print "Player 2 has score of: ", Score2
		else:
		   	print "Player 2 Wins!"
		        Score2 -= 1
			print "Player 1 has score of: ", Score1
			print "Player 2 has score of: ", Score2
	
		if Score1 == 0:
			print "Player 1 wins the best of 3"
		if Score2 == 0:
			print "Player 2 wins the best of 3"
	retry()	    
scorer()  

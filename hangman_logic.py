word = "EVAPORATE"
letters_guessed = []

empty_char = ['_' for i in range(len(word))]
combine = ''.join(empty_char)

while '_' in empty_char:
	letter = input("Guess a letter in the word: ")
	letter = letter.upper()
	
	if letter in letters_guessed:
		letter = ''
		print("Already guessed!")
	elif letter in word:
		letters_guessed.append(letter)
		for i in range(len(word)):
			if word[i] == letter:
				empty_char[i] = letter
		print(''.join(empty_char))
	else:
		if letter not in word:
			print("Letter not in word, guess again!")
			letters_guessed.append(letter)
			print("Letters already guessed:{} ".format(letters_guessed))
			print(''.join(empty_char))

	if '_' not in empty_char:
		print("You win!")
		break

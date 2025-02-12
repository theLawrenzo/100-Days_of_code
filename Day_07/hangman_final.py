#!/usr/bin/python3

import random
import hangman_art
import hangman_words

lives = 6

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""

for letter in chosen_word:
	placeholder += '_'

print(f"Word to guess: {placeholder}")

correct_letters = []
game_over = False

while not game_over:
	display = ""

	print(f"**************************** {lives}/6 LIVES LEFT "
			"****************************")
	
	guess = input('Guess a letter: ').lower()

	if guess in correct_letters:
		print(f"You've already guessed {guess}")

	for letter in chosen_word:
		if guess == letter:
			display += guess
			correct_letters.append(guess)
		elif letter in correct_letters:
			display += letter
		else:
			display += '_'

	print(f"Word to guess: {display}")
	if guess not in chosen_word:
		lives -= 1
		if lives > 0:
			print(f"You guessed '{guess}',"
				" that is not in the word. You lose a life!")
		else:
			game_over = True
			print(f"IT WAS '{chosen_word}'. YOU LOSE!")
	elif display == chosen_word:
		game_over = True
		print("CONGRATULATIONS! YOU WIN.")

	print(hangman_art.stages[lives])

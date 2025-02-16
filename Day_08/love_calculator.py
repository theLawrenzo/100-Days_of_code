#!/usr/bin/python3

def calculate_love_score(name1='Laurens', name2='Maris'):
	names_together = (name1 + name2).upper()

	# Variables to store the number of letters from 'LOVE' and 'TRUE' found in both names
	num_in_true = 0
	num_in_love = 0

	# loop to traverse through each word
	for letter in 'TRUE':
		num_in_true += names_together.count(letter)

	for char in 'LOVE':
		num_in_love += names_together.count(char)

	print(f'{num_in_true}{num_in_love}')

calculate_love_score('lawrence', 'damaris')

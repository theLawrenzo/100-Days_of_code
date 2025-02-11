#!/usr/bin/python3

import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
	  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')

number_of_alphabets = int(input('How many letters would you like in your password?\n'))
number_of_symbols = int(input('How many symbols would you like?\n'))
number_of_digits = int(input('How many digits would you like?\n'))

random_password = []
password = ""

if number_of_alphabets > 0 and number_of_symbols > 0 and number_of_digits > 0:
	for alpha in range(0, number_of_alphabets):
		random_password.append(random.choice(alphabets))

	for symbol in range(0, number_of_symbols):
		random_password.append(random.choice(symbols))
	
	for digit in range(0, number_of_digits):
		random_password.append(random.choice(digits))

	print('['+','.join(random_password)+']')
	random.shuffle(random_password)
	print('['+','.join(random_password)+']')

	for a in random_password:
		password += a
	print(f'Your password is: {password}')
else:
	print("Sorry can't generate password. Invalid entry!'")

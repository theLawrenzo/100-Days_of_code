#!/usr/bin/python3

alphabet = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
	'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
	's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text="Hello, World!", shift_amount=1):
	output_text = ""

	# Iterate through every letter in the input text given by the user
	for letter in original_text:
		# set the size of the new position of each letter
		shifted_position = shift_amount + alphabet.index(letter)
		# trick to get the correct amount to shift each letter by:
		# When a smaller number is used as the first parameter of a mod operator, it would alway return the first param
		# And it would always return the remainder of the operation when the first param is bigger than the second
		shifted_position %= len(alphabet)
		output_text += alphabet[shifted_position]

	print(f"Here is the encoded result: {output_text}")

encrypt(original_text=text, shift_amount=shift)

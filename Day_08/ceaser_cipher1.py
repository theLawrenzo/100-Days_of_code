#!/usr/bin/python3

alphabet = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
	'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
	't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text="Hello, World!", shift_amount=1):
    encoded_text = ""

    if len(original_text) > 0:
        for letter in original_text:
            places = alphabet.index(letter) + shift_amount + 1

            if shift_amount <= 13 >= alphabet.index(letter):
                encoded_text += alphabet[places]
            elif shif_amount > 13 < alphabet.index(letter):
                encoded_text += alphabet[places - (len(alphabet) - 1)]
            elif 

    print(f'Here is the encoded result: {encoded_text}')

encrypt(text, shift)

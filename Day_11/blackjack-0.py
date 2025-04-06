#!/usr/bin/python3
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_request = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if play_request == 'y':
    user_cards = [random.choice(cards), random.choice(cards)]
    comp_cards = [random.choice(cards), random.choice(cards)]

    print(user_cards)
    print(comp_cards)
else:
	print('\n')

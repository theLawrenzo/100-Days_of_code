#!/usr/bin/python3

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list = [rock, paper, scissors]

computer_choice = random.choice(choice_list)

user_choice = int(input('What do you choose? Type 0 for Rock,'
			' 1 for Paper or 2 for Scissors.\n'))

if user_choice <= 2 and user_choice >= 0:
	print(choice_list[user_choice])
	print('Computer chose:')
	print(computer_choice)

if user_choice > 2 or user_choice < 0:
	print("Invalid option. You Lose!")
elif user_choice == choice_list.index(computer_choice):
	print("It's a draw!")
elif user_choice == 0:
	if computer_choice == choice_list[1]:
		print('You Lose!')
	elif computer_choice == choice_list[2]:
		print('You win!')
elif user_choice == 1:
	if computer_choice == choice_list[0]:
		print('You Win!')
	elif computer_choice == choice_list[2]:
		print('You Lose!')
elif user_choice == 2:
	if computer_choice == choice_list[0]:
		print('You Lose!')
	elif computer_choice == choice_list[1]:
		print('You Win!')

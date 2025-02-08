100-Days_Of_Code

DAY 04 - Randomization and Python List


NEW THINGS I LEARNED:
	- Randomization is the science of making undeterministic selection.
	- In python a list is a data structure that lets you store multiple elements in a variable. 


EXERCISES:

i. HEADS OR TAILS PICKER:
- Write a program that generates a random number and prints either heads or tails depending on
  the number generated.


	PSEUDOCODE:
  		. create a file 'head_tail.py
		. begin file with '#!/usr/bin/python3'
		. import the random module
		. use the randint() function of the random module to generate a random number
		. create a conditional block
			if num_generated % 2 == 0:
				print 'Heads'
			else:
				print 'Tails'


ii. RANDOM BILL PAY PERSON PICKER
- Write a program that selects a name randomly from a list of names

	PSEUDOCODE:
		. create a file 'who_pays.py'
		. begin file with '#!/usr/bin/python3'
		. import the random module
		. create a variable that stores a list containing the names of six friends
		. pass the list to the random.choice() function to make a random selection of any name
		. print out the name selected


PROJECT OF THE DAY:

. ROCK PAPER SCISSORS:
- Write a program that simulates the famous rock-paper-scissors game.

	GAME RULES:
		. Scissors wins agianst Paper
		. Paper wins agianst Rock
		. Rock wins against Scissors

	PROGRAM_CHALLANGES:
		. How to get the computer to choose and make its choice random each time

	PSEUDOCODE:
		. Create a file 'rock_paper_scisssors.py
		. Begin file with '#!/usr/bin/python3'
		. import the random module
		. create 3 variables to store 3 different ASCII arts of: rock, paper, scissors.
		. create a list 'choice_list' that holds this items - the rock, paper, scissors variables
		. create another variable called computer_choice
		. pass the list to the random.choice() function to make a random choice for the computer
		  and store its return value in the computer_choice variable
		. create another variable 'user_choice'
		. create an input statement that has its input converted to integer with the int function
		  and store the user input in the user_choice variable. The user input should be between
		  0, 1, and 2
		. Create a conditional block:
			if choice_list[user_choice] == choice_list[0]:
				if computer_choice == 1:
					print user_ascii art
					print('Computer chose:')
					print computer_ascii art
					print('You lose')
				elif computer_choice == 2:
					print('You win')
			elif choice_list[user_choice] == choice_list[1]:
				if computer_choice == 0:
					print('You Win')
				elif computer_choice == 2:
					print('You Lose')
			elif choice_list[user_choice] == choice_list[2]:
				if computer_choice == 0:
					print('You Win')
				elif computer_choice == 1:
					print('You Lose')
			else:
				print('You Loose')

			if choice_list[user_choice] == computer_choice:
				print("It's a draw!')

#!/usr/bin/python3

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print('Welcome to Treasure Island.\nYour Mission is to find the treasure, but becareful.')
choice = input('There are three routes in front of you, which do you want to take? Left, Right, or Middle: ')
if choice == 'Right' or choice == 'right':
	print('Game Over.')
elif choice == 'left' or choice == 'Left':
	print('You have gotten to the lake lagoon')
	choice = input('Do you want to swim or wait for a boat? Swim or Wait: ')
	if choice == 'swim' or choice == 'Swim':
		print('You got eaten by crocodiles!')
		print('\tGame Over.')
	elif choice == 'wait' or choice == 'Wait':
		print('\tEnjoy the ride to the other side')
		choice = input('You are at a cross road, do you want to journey through the cave of echoes or the forest of reflection? Cave or Forest: ')
		if choice == 'Cave' or 'cave':
			print('You got eaten by wild bats!')
			print('\tGame Over.')
		else:
			print('You are back at the beginning!')
else:
	print('Congratulations you found the treasure!')
	print('\tYou Win.')

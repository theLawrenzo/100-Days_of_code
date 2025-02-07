DAY 3: 100-Days_Of_Code

- What I learned:
	. Python Conditional statement
		. if conditional statement
		. if-else conditional statement
		. multiple if statements
	. Modulo operator (%)

EXERCISE:
i. Write a program to check a user input if it is odd or even:
	PSEUDOCODE:
		. create a file odd_even.py
		. Begin file with '#!/usr/bin/python3'
		. Prompt user for input
		. Convert user input to float
		. Create a conditional statement block:
			. if user_input % 2 == 0:
				print 'Even'
			. else:
				print 'Odd'

ii. BMI calculator:
	PSEUDOCODE:
		. create a file bmi_calc.py
		. begin file with '#!/usr/bin/python3'
		. prompt user to give height
		. prompt user to give weight
		. calculate the bmi
			bmi = weight / (height ** 2)
		. create a conditional block to interpret bmi:
			if bmi < 18.5:
				print 'Underweiht'
			elif bmi < 25:
				print 'Normal weight'
			else:
				print 'Over weight'


iii. pizza delivery program:
- Write a program that works out the final price of an order based on users preference.
	. Small Pizza (S): $15
	. Medium Pizza (M): $20
	. Large Pizze (L): $25
	. Add pepperoni for small pizza (Y or N): +$2
	. Add pepperoni for medium or large pizza (Y or N): +$3
	. Add extra cheese for any size pizza (Y or N): +$1

	PSEUDOCODE:
		. create a file pizza_order.py
		. begin file with '#!/usr/bin/python3'
		. create a variable 'price' with value zero (0)
		. prompt user to give size of pizza they want
		. create conditional block:
			if size == s:
				. update price to be 15
				ask user if they want pepperoni:
					if pepperoni == 'y':
						. update price to be price += 2
			elif size == m:
				. update price to be 20
				ask user if they want pepperoni:
					if pepperoni == 'y':
						. update price to be += 3
			else:
				. update price to be 25
				ask user if they want pepperoni:
					if pepperoni == 'y':
						. updadte price to be +=3
		. ask user if they want extra cheese
		. create a conditional block:
			if extra_cheese == 'y':
				price += 1
		. print the final price to the user.


PROJECT OF THE DAY:
	. Build a treasure hunting game:
	- User gets to make choices that determines the outcome of the game.

	PSEUDOCODE:
		. create file treasure_hunt.py
		. begin file with #!/usr/bin/python3
		. print 'Welcome to the Treasue Island. Your mission is to find the treasure'
		. Create a conditional block with multiple if statements and nested if statements
		. if the user takes a wrong turn:
			print game over
		. if the user takes all the right turns till the last one:
			print 'Congratulations you found the treasure'

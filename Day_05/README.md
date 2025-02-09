100-Days_Of_Code

DAY_05: For Loop, Range and Code Block

OBJECTIVE:
	By the end of this lecture I ought to have an indepth knowledge
	of how for loop work in python and how to apply them into real
	world scenerios to solve real world problems.


NEW THINGS I LEARNED:
	i. For Loops in python:
	- First a loop is the process of repeating something over and over
	again till a condition is met or for a specified number of times.

	For loops in python are specifically built for operation with sequences.
	They take the form of the 'for' keyword with a temporary variable, followed
	by the in keyword, and then the sequences.
	Each item in the sequence is assigned to the temporary variable beginning
	from the item at index 0.

EXERCISES:

i. MAX FUNCTION:
- Write a function that traverses through a list of items (numbers), then selects the
highest number from the list.
	. Implement the program using a for loop

	PSEUDOCODE:
		. create a file 'max.py'
		. begin file with '#!/usr/bin/python3'
		. create a list 'num_list' and populate it with different sized numbers
		. create another variable 'max_num' and assign it with the value of 0
		. create a for loop that traverses through each item in the list
			for num in num_list:
				if num > max_num:
					max_num = 0
		. print the max_num variable value


ii. RANGE ADDER
- Write a function that adds up all the numbers in a range of numbers

	PSEUDOCODE:
		. create a file 'range_add.py'
		. begin file with '#!/usr/bin/python3'
		. create a variable 'total' and assign it the value 0
		. creata a for loop that goes from 1 to a range of 101
			for num in range(1, 101):
				total += num

		. print the value of total

iii. FIZZBUZZ CHALLENGE
- Write a program that prints all the numbers from 1 to 100:
	. if the number is divisible by 3 then print 'Fizz' instead
	. if the number is divisible by 5 print 'Buzz' instead
	. if the number is divisible by 5 and 3 print 'FizzBuzz' instead

	PSEUDOCODE:
		. create a file 'fizz_buzz.py'
		. begin file with '#!/usr/bin/python3'
		. create a for loop that iterates from 1 to a 100 using range
		. with the loop create a conditional statement
			. if number is divisble by 3 and not by 5
				. then print 'Fizz'
			. else if number is divisible by 5 and not by 3
				. then print 'Buzz'
			. else if number is divisible by both 5 and 3
				. then print 'FizzBuzz'
			. else
				. print the number

PROJECT OF THE DAY:

PY-PYTHON GENERATOR PROGRAM:
- Write a program that genertes a random password for a user based on specific request.
	. ask user for number of characters to know how many characters to generate
	. ask the user for the number of symbols to include in password
	. ask the user for the number of digits to include in password

	PSEUDOCODE:
		1 create a file 'password_generator.py'
		2 begin file with '#!/usr/bin/python3'
		3 import the random module
		4 create a variable 'alphabets' that stores a list of all the alphabetical characters
		  both uppercase and lowercase
		5 create another variable 'symbols' that holds some special symbol that can be used
		  in a password
		6 create another variable 'digits' that holds a list of digits from 0 to 9
		7 create three input elements, one for alphabet, another for symbol and the other for
		  digit, and store the user inputs in the 3 varaibles
		8 convert all the user inputs to integers using the int function
		9 create an empty list 'random_password'
		10 create a conditional statement to check if value given by user is an integer
		11 create a for loop that iterates from 0 to the digit passed for number of alphabets.
		12 use the random.choice() to generate a random choice on each iteration, and append
		   it to the list on each iteration
		13 create another conditional to check if value given for number of symbols is a digit
		14 Repeat step 11, only use the digit passed for number of symbols
		15 Repeat step 12
		16 Repeat step 13(17), 14(18), and 15(19) again but only use the number giving for
		   number of digits with the for loop.
		20 call the random.shuffle() function and pass it the random_password list
		21 create a variable 'password_string' assigning it an empty string literal
		22 create another for loop and iterate through the random_password list and
		   append to it all the items of the list
		23 print out the new password generated.


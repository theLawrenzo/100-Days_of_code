100-Days_Of_Code

DAY_08

OBJECTIVE OF THE DAY - Build a ceaser cypher program

By the end of the day I'd have learned all about functions with inputs
arguments and parameters.
	. The difference between argument and parameters

And at the end of the day, I combined all of the concepts I've learned
together to build a ceaser cypher program.



NEW THIGS LEARNED

	. Difference between function Parameter and Argument:
	  A Function parameter is the name (identifier) given to the
	  variable that's in the function definition, why the argument
	  is the actual value of the data being passed.



EXERCISES

i. Life In Weeks:
 - Write a program that calculates how many weeks you have left to live
   assuming you'll live only 90 years. Weeks should should be calculated
   based on user's aged passed as argument to the function that calculates
   the age.
	PSEUDOCODE:
		. Create a file 'life_in_weeks.py'
		. begin file with '#!/usr/bin/python3'
		. create a function 'life_in_weeks' function has one
		  parameter 'age'
		. create a variable weeks_in_a_year = 365 // 7
		. creata another variable max_age = 90
		. create another variable weeks_left = (max_age - age) *
							weeks_in_a_year
		. print value of variable 'weeks_left'

ii. Caeser cipher 0
- Write a program that takes three input, the first is a command that insturts
the program on what to do with the second which is a text, and then the third
determines how the operation would be carried out on the second
	. Create a function 'encrypt' that takes two arguments: 'original_text'
	  and 'shift_amount'
	
	PSEUDOCODE:
		. create a file 'caeser_cipher0.py'
		. begin file with '#!/usr/bin/python3'
		. create a list that of all 26 alphabets in lowercase
		. declare an input statement asking the user to either type
		  'encode' or 'decode' and save value in a variable called
		  'crypt_command', make input to be in lowercase
		. declare another input statement asking user to enter a text
		  then save value in a variable 'text', make the input lower
		. declare another input statement asking the user to give an
		  integer to determine how many places each letter would be
		  shifted
		. create a function 'encrypt', it takes two arguments:
		  'original_text' and 'shift_amount'
			INSIDE FUNCTION:
			. create an empty string variable 'output_text'
			. create a for loop to cycle through each letter of the
			  original_text
			INSIDE THE FOR LOOP:
			. create a variable that would be equal to the sum of
			  the index number of each letter plus the shift_amount
			  on each iteration/cycle. 'new_position_size'
			. use the modulo operator to determine what the new
			  index of the letter should be, by modulating the
			  new_position_size by the length of the alphabet list
			. concatenate alphabet at index equal to the new_index
			  gotten from the previous step, to the output_text
			  empty string variable, previously created
			OUTSIDE THE FOR LOOP:
			. print out 'Here is the encoded result' plus the value
			  of the 'output_text' variable


PROJECT OF THE DAY - Fully functioning caeser cipher encryptioning program

#!/usr/bin/python3

weight = float(input('Please enter your weight: '))
height = float(input('Please enter your height: '))

bmi = weight / (height ** 2)

# Conditional Block for BMI interpretation

if bmi < 18.5:
	print('Underweight')
elif bmi < 25:
	print('Normal Weight')
else:
	print('Over Weight')

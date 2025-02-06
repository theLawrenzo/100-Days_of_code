#!/usr/bin/python3

print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))
tip = tip / 100 + 1
each_member_cost = round(bill * tip / people, 2)
print('Each person should pay ${}'.format(each_member_cost))

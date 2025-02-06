#!/usr/bin/python3

print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))
tip_in_percent = tip / 100 + 1
bill_per_person = round(bill * tip_in_percent / people, 2)
print('Each person should pay ${}'.format(bill_per_person))

#!/usr/bin/python3

def life_in_weeks(age):
	weeks_in_a_year = 365 // 7
	max_age = 90
	weeks_left = (max_age - age) * weeks_in_a_year

	print(f"You have {weeks_left} weeks left.")

life_in_weeks(56)

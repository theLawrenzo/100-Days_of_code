#!/usr/bin/python3

def is_leap_year(year):
	if year % 4 == 0:
		if year % 100 == 0 and year % 400 == 0:
			return True
		elif year % 100 == 0 and year % 400 != 0:
			return False
		elif year % 100 != 0 and year % 400 == 0:
			return True
		elif year % 100 != 0 and year % 400 != 0:
			return False
	else:
		return False


print(f"2024 = {is_leap_year(2024)}")
print(f"2020 = {is_leap_year(2020)}")
print(f"2400 = {is_leap_year(2400)}")
print(f"1989 = {is_leap_year(1989)}")

#!/usr/bin/python3

import random

random_num = random.random() * 1000

random_num = round(random_num)

if random_num % 2 == 0:
	print("Heads")
else:
	print("Tails")

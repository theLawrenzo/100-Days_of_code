#!/usr/bin/python3

num_list = [77, 69, 135, 299, 229, 145, 250, 285, 189, 287, 305, 248, 298]
max_num = 0

for num in num_list:
	if num > max_num:
		max_num = num

print(max_num)

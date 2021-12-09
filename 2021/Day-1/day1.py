#!/usr/bin/env python3

with open('input.txt', 'r') as f:
	input = f.readlines()

vals = iter(input)
prev = int(input[0])
next(vals)

answer = 0

for val in vals:
	if int(val) > prev:
		answer += 1
	prev = int(val)

print(f'Answer = {answer}')

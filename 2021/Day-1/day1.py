#!/usr/bin/env python3

with open('input.txt', 'r') as f:
	input = f.readlines()

prev = int(input[0])
answer = 0

for val in input[1:]:
	if int(val) > prev:
		answer += 1
	prev = int(val)

print(f'Answer = {answer}')

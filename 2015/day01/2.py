#!/usr/bin/env python3.9

f = open("input.txt", "r")

s = f.read()

current_position = 0
idx = 0

for i in list(s):
    idx += 1
    if i == '(':
        current_position += 1
    elif i == ')':
        current_position -= 1

    if current_position == -1:
        print(idx)
        exit(1)

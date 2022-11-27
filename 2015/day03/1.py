#!/usr/bin/env python3.9

def uniq(sequence):
    already = []
    res = []
    for i in sequence:
        if i not in already:
            res.append(i)
            already.append(i)
    return res

f = open("input.txt", "r")
s = f.read()
directions = list(s)

x = 0
y = 0
histories = [{'x': x, 'y': y}]

for d in directions:
    if d == '^':
        y += 1
    elif d == 'v':
        y -= 1
    elif d == '>':
        x += 1
    elif d == '<':
        x -= 1

    histories.append({'x': x, 'y': y})

#print(len(histories))
print(len(uniq(histories)))


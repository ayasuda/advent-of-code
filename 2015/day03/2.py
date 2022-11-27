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


s_x = 0
s_y = 0
r_x = 0
r_y = 0
histories = [{'x': s_x, 'y': s_y}]

i = 0
for d in directions:
    i += 1
    is_robo = True if i % 2 else False
    if is_robo:

        if d == '^':
            r_y += 1
        elif d == 'v':
            r_y -= 1
        elif d == '>':
            r_x += 1
        elif d == '<':
            r_x -= 1
        histories.append({'x': r_x, 'y': r_y})
    else:

        if d == '^':
            s_y += 1
        elif d == 'v':
            s_y -= 1
        elif d == '>':
            s_x += 1
        elif d == '<':
            s_x -= 1
        histories.append({'x': s_x, 'y': s_y})

print(len(histories))
print(len(uniq(histories)))

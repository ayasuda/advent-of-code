#!/usr/bin/env python3.9

total = 0
with open("input.txt", "r") as f:
    for line in f:
        sl, sw, sh = line.split("x")
        l = int(sl)
        w = int(sw)
        h = int(sh)

        sides = [l, w, h]
        sides.sort()

        around = 2 * sides[0] + 2 * sides[1]
        bow = l * w * h

        total += (around + bow)


print(total)

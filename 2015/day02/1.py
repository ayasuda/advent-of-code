#!/usr/bin/env python3.9

total = 0
with open("input.txt", "r") as f:
    for line in f:
        sl, sw, sh = line.split("x")
        l = int(sl)
        w = int(sw)
        h = int(sh)

        base_size = 2 * l * w + 2 * w * h + 2 * h * l
        extra_size = min([ l * w, w * h, h * l])
        total += base_size
        total += extra_size

print(total)

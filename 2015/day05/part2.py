#!/usr/bin/env python3.9

VOWELS = list("aeiou")
DISALLOWED = ["ab", "cd", "pq", "xy"]

def is_nice(line):
    # e.g. xy...xy
    contains_pair = False

    # e.g. xyx
    contains_lol = False

    previous_character = ''
    two_previous_character = ''
    pairs = []

    for c in list(line):
        current_pair = f'{previous_character}{c}'
        if current_pair in pairs[:-1]:
            contains_pair = True
        pairs.append(current_pair)

        if c == two_previous_character:
            contains_lol = True

        two_previous_character = previous_character
        previous_character = c

    if contains_pair and contains_lol:
        return True
    return False


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        cnt = 0
        for line in f:
            if is_nice(line):
                cnt += 1
        print(cnt)

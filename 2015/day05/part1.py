#!/usr/bin/env python3.9

VOWELS = list("aeiou")
DISALLOWED = ["ab", "cd", "pq", "xy"]

def is_nice(line):
    vowels_count = 0
    has_three_vowels = False
    contains_twice = False
    contains_disallowed = False
    previous_character = ''

    for c in list(line):
        if c in VOWELS:
            vowels_count += 1
        if previous_character == c:
            contains_twice = True
        if f'{previous_character}{c}' in DISALLOWED:
            contains_disallowed = True
        previous_character = c
    if vowels_count >= 3:
        has_three_vowels = True

    print(f'has three vowels: {has_three_vowels}')
    print(f'contains twice: {contains_twice}')
    print(f'contains disallowed: {contains_disallowed}')
    if has_three_vowels and contains_twice and not contains_disallowed:
        return True
    return False


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        cnt = 0
        for line in f:
            if is_nice(line):
                cnt += 1
        print(cnt)

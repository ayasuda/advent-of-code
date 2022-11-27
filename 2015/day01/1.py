#!/usr/bin/env python3.9

f = open("input.txt", "r")

s = f.read()

print(s.count('(') - s.count(')'))

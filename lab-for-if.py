#!/usr/bin/env python3

## fszostak(2020) Python 3.8 Code Snippets
#
#  contributor: https://github.com/cbarbado
#
#  python for if examples

t = (1, 2 , 3)

print(type(t), t)

for n in t:
    print(n)

print([n for n in t if n > 1])

[print(n) for n in t if n > 1]

r = [str(n) for n in t if n > 1]
print(r)

for i in [n for n in t if n > 1]:
    print(type(i), i)

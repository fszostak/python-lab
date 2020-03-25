#!/usr/bin/env python3

## fszostak(2020) Python 3.8 Code Snippets
#
#  Function decorators

from modules.decorators import ClassRepeat, repeat

@repeat
def multiply(a, b):
    print(f'Multiply {a}*{b}')
    return a * b

@repeat(num_times=5)
def divide(a, b):
    print(f'Divide {a}/{b}')
    return a / b

@ClassRepeat()
def sum(a, b):
    print(f'Sum {a}+{b}')
    return a + b

@ClassRepeat(num_times=3)
def substract(a, b):
    print(f'Substract {a}-{b}')
    return a - b


print("@repeat")
print("Multiply(10, 20) =", multiply(10, 20))
print()

print("@repeat(num_times=4)")
print("divide(10, 20) =", divide(10, 20))
print()

print("@ClassRepeat()    <= TODO: remove ()")
print("sum(10, 20) =", sum(10, 20))
print()

print("@ClassRepeat(num_times=1)")
print("substract(10, 20) =", substract(10, 20))
print()
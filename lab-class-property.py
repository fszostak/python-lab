#!/usr/bin/env python3

## fszostak(2020) Python Code Snippets
#
#  Class property 

import sys

class MyClass:

    def __init__(self, x):
        self._attr = x

    @property
    def attr(self):
        print(f'MyClass.attr property {self._attr}')
        return self._attr

    @attr.setter
    def attr(self, value):
        print(f'MyClass.attr setter value={value}')
        self._attr = value

## main function
#
def main(argv):
    # get MyClass instance
    instance = MyClass("aaa")
    print('instance.attr =', instance.attr)

    # change attr value
    instance.attr = "bbb"
    print('instance.attr =', instance.attr)

    # change attr value
    instance.attr = "ccc"
    print('instance.attr =', instance.attr)

## __main__
#
if __name__ == "__main__":
    main(sys.argv[1:])
    
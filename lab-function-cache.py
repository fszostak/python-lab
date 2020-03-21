#!/usr/bin/env python3

## fszostak(2020) Python Code Snippets
#
#  Function cache with functools 

import sys
from functools import lru_cache

@lru_cache()
def f(x):
    print(f'execute f(x) = f({x}) return {x + x}')
    return(x + x)

## main function
#
def main(argv):
    print(f'result f(aaa) = {f("aaa")}')
    print(f'result f(aaa) = {f("aaa")}')
    print(f'result f(aaa) = {f("aaa")}')
    print(f'result f(aaa) = {f("aaa")}')
    print(f'result f(aaa) = {f("aaa")}')
    print(f'result f(aaa) = {f("aaa")}')
    print(f'result f(ccc) = {f("ccc")}')
    print(f'result f(aaa) = {f("aaa")}')
    print(f'result f(aaa) = {f("aaa")}')
    print(f'result f(ccc) = {f("ccc")}')
    print(f'result f(aaa) = {f("aaa")}')
    print(f'result f(bbb) = {f("bbb")}')
    print(f'result f(bbb) = {f("bbb")}')
    print(f'result f(aaa) = {f("aaa")}')
    print(f'result f(bbb) = {f("bbb")}')
    print(f'result f(bbb) = {f("bbb")}')
    print(f'result f(bbb) = {f("bbb")}')
    print(f'result f(aaa) = {f("aaa")}')
    print(f'result f(bbb) = {f("bbb")}')
    print(f'result f(ccc) = {f("ccc")}')
    print(f'result f(ccc) = {f("ccc")}')
    print(f'result f(ccc) = {f("ccc")}')
    print(f'result f(ccc) = {f("ccc")}')
    print(f'result f(aaa) = {f("aaa")}')
    print(f'result f(ccc) = {f("ccc")}')
    print(f'result f(ccc) = {f("ccc")}')
    print(f'result f(ccc) = {f("ccc")}')
    print(f'result f(ccc) = {f("ccc")}')
    print(f'result f(aaa) = {f("aaa")}')

## __main__
#
if __name__ == "__main__":
    main(sys.argv[1:])

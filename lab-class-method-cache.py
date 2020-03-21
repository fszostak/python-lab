#!/usr/bin/env python3

## fszostak(2020) Python 3.8 Code Snippets
#
#  Class method cache 

import sys
from functools import lru_cache
class MyClass:

    def __init__(self, prop1, prop2):
        self._prop1 = prop1
        self._prop2 = prop2

    def __str__(self):
        return f'MyClass() prop1={self._prop1} prop2={self._prop2}'

    ''' property prop1 '''
    @property
    def prop1(self):
        print(f'MyClass.prop1 getter {self._prop1}')
        return self._prop1

    @prop1.setter
    def prop1(self, value):
        print(f'MyClass.prop1 setter prop1={value}')
        self._prop1 = value
        self.cache_clear()

    ''' property prop2 '''
    @property
    def prop2(self):
        print(f'MyClass.prop2 getter {self._prop2}')
        return self._prop2

    @prop2.setter
    def prop2(self, value):
        print(f'MyClass.prop2 setter prop2={value}')
        self._prop2 = value
        self.cache_clear()

    ''' actions '''
 
    def concat(self):
        print('MyClass.concat() executed')
        return self.prop1 + self.prop2
    
    def invert(self):
        print('MyClass.invert() executed')
        temp = self.prop1
        self.prop1 = self.prop2
        self.prop2 = temp

    @lru_cache()
    def cachedConcatValue(self, value):
        result = self.prop1 + value + self.prop2
        print(f'MyClass.cachedConcatValue({result}) executed')
        return result

    def cache_clear(self):
        print(f'MyClass.cache_clear() executed')
        self.cachedConcatValue.cache_clear()
        

## pressKey function
def pressKey(next, press='...'):
    input(press)
    print(f'\n\n{next.upper()}')

## main function
#
def main(argv):
    print('\nget MyClass instance')
    instance = MyClass("aaa", "bbb")
    print('instance =', str(instance))

    pressKey('show concat example')
    print('\ninstance.concat =', instance.concat())

    pressKey('show invert example')
    instance.invert()
    print('\ninstance.invert()')
    print('instance =', str(instance))

    pressKey('show cachedConcatValue example')
    print('\ninstance.cachedConcatValue =', instance.cachedConcatValue(','))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(','))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(':'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(':'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(':'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue('.'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(':'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue('.'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue('.'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(':'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(','))
    print('instance.cachedConcatValue =', instance.cachedConcatValue('.'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(','))
    print('instance.cachedConcatValue =', instance.cachedConcatValue('.'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(':'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(','))
    print('instance.cachedConcatValue =', instance.cachedConcatValue('.'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(','))

    pressKey('properties changed')
    instance.prop1 = 'ccc'
    instance.prop2 = 'ddd'
    print('instance =', str(instance))

    print('\ninstance.cachedConcatValue =', instance.cachedConcatValue(','))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(','))
    print('\ninstance.cachedConcatValue =', instance.cachedConcatValue('#'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue('.'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue('#'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(','))
    print('instance.cachedConcatValue =', instance.cachedConcatValue('.'))

    pressKey('invert properties again')
    print('\ninstance.invert()')
    instance.invert()
    print('instance =', str(instance))

    pressKey('invert properties again')
    print('\ninstance.cachedConcatValue =', instance.cachedConcatValue('#'))
    print('instance.cachedConcatValue =', instance.cachedConcatValue(','))
    print('instance.cachedConcatValue =', instance.cachedConcatValue('#'))

## __main__
#
if __name__ == "__main__":
    main(sys.argv[1:])

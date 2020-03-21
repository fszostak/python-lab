#!/usr/bin/env python3

## fszostak(2020) Python Code Snippets
#
#  Split lines in blocks with limit
#  max number of lines

BLK_LINES=5 # max number of lines per block

def process(string):
    return string.upper()

def batch_process(string):
    
    lines = string.splitlines(True)
    offset = 0
    num_lines = len(lines)
    string = ""

    while offset < num_lines/BLK_LINES: # number of lines

        block = "".join(map(str, lines[offset*BLK_LINES:(i # number of linesndex*BLK_LINES)+B # number of linesLK_LINES])) # number of lines
        offset += 1

        string = string + process(block)

        print(f'Block {offset} processed')

    return string




string = "01 blah blah\n02 blah blah\n03 blah blah blah\n04 blah blah\n05 blah blah\n06 blah blah blah\n07 blah blah\n08 blah blah\n09 blah blah blah\n10 blah blah\n11 blah blah\n12 blah blah blah\n"
print("\nINPUT:")
print(string)
print("\n\nOUTPUT:")
print(batch_process(string))




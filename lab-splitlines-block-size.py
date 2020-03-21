#!/usr/bin/env python3

## fszostak(2020) Python Code Snippets
#
#  Split lines in blocks with limit
#  max number of bytes

BLK_SIZE=9  # max number of bytes per block

def process(string):
    return string.upper()

def batch_process(string):
    
    block = response = ""
    offset = n = 0
    line_size = string.find("\n")

    while line_size > 0:

        if offset+line_size > BLK_SIZE:
            response = response + process(block)
            block = ""
            print(f'Block {n} processed')
            n += 1

        block = block + string[offset:offset+line_size+2]

        offset = offset + line_size+2
        line_size = string[offset:].find("\n") 

    block = block + string[offset:]
    if block != "":
        response = response + process(block)
        print(f'Block {n} processed')

    return response



# basic test
string = "01 blah blah\n02 blah blah\n03 blah blah blah\n04 blah blah\n05 blah blah\n06 blah blah blah\n07 blah blah\n08 blah blah\n09 blah blah blah\n10 blah blah\n11 blah blah\n12 blah blah blah\n"
print("\nTEST 1 - INPUT:")
print(string)
print("\n\nOUTPUT:")
print(batch_process(string))

# last line great than previous line
string = "01 blah blah\n02 blah blah\n03 blah blah\n04 blah blah\n05 blah blah\n06 blah blah\n07 blah blah\n08 blah blah\n09 blah blah\n10 blah blah\n11 blah blah\n12 blah blah blah\n"
print("\nTEST 2 - INPUT:")
print(string)
print("\n\nOUTPUT:")
print(batch_process(string))

# last line less than previous line
string = "01 blah blah\n02 blah blah\n03 blah blah\n04 blah blah\n05 blah blah\n06 blah blah\n07 blah blah\n08 blah blah\n09 blah blah\n10 blah blah\n11 blah blah\n12 blah\n"
print("\nTEST 3 - INPUT:")
print(string)
print("\n\nOUTPUT:")
print(batch_process(string))

# with \r\n
string = "01 blah blah\r\n02 blah blah\r\n03 blah blah\r\n04 blah blah\r\n05 blah blah\r\n06 blah blah\r\n07 blah blah\r\n08 blah blah\r\n09 blah blah\r\n10 blah blah\r\n11 blah blah\r\n12 blah blah blah\r\n"
print("\nTEST 4 - INPUT:")
print(string)
print("\n\nOUTPUT:")
print(batch_process(string))

# without newline in last line
string = "01 blah blah\r\n02 blah blah\r\n03 blah blah\r\n04 blah blah\r\n05 blah blah\r\n06 blah blah\r\n07 blah blah\r\n08 blah blah\r\n09 blah blah\r\n10 blah blah\r\n11 blah blah\r\n12 blah"
print("\nTEST 5 - INPUT:")
print(string)
print("\n\nOUTPUT:")
print(batch_process(string))












#!/usr/bin/env python3

import sys
import re

translate_table = ['a','b','c','d','e','f','g','h','i','j']

def transform(number):
    out = [] 
    number = number[::-1]
    counter = 0;
    for x in number:
        if x == '1':
            out.append(translate_table[counter])
        else:
            out.append('0')
        counter += 1
    output = ''.join(str(x) for x in out)
    return output


def my_printf(format_string,param):
    matcher = re.search("#b", format_string)
    if not matcher:
        print(format_string)
        return
    
    number = bin(int(param))[2:]
    output = transform(number)

        
    print(out)
    
    

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

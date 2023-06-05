#!/usr/bin/env python3

import sys
import re

def transform(number):
    out = [] 
    length = len(number)
    i = -1
    for x in range(length):
        
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

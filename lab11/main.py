#!/usr/bin/env python3

import sys
import re

def transform(number, length):
    return int((number*2)/length)


def my_printf(format_string,param):
    matcher = re.search("#a", format_string)
    if not matcher:
        print(format_string)
        return
    
    number = int(param)
    length = len(str(number))
    if(number == 0):
        out = format_string.replace(matcher.group(), '0')
    else:
        if(param[0] == '-'):
            length -= 1

        result = transform(number, length)

        if(result % 2 == 0):
            out = format_string.replace(matcher.group(), str(result))
        else:
            out = format_string.replace(matcher.group(), str(hex(result)).replace('0x', ''))
        
    print(out)
    
    

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

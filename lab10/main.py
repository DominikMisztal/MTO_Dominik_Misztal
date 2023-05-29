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
    length = len(param)
    result = transform(number, length)

    if(result % 2 == 0):
        format_string.replace(matcher, str(result))
    else:
        format_string.replace(matcher, str(hex(result)))
        
    print(format_string)
    
    

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

#!/usr/bin/env python3

import sys
import re

def transform(number, length):
    return int((number*2)/length)


def my_printf(format_string,param):
    matcher = re.search("#b", format_string)
    if not matcher:
        print(format_string)
        return
    
    number = str(int(param))
    
        
    print(out)
    
    

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

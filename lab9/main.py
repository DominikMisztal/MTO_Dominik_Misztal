#!/usr/bin/env python3

import sys
import re


def my_printf(format_string,param):
    matcher = re.search("#a", format_string)
    if not matcher:
        print(format_string)
        return
    
    number = int(param)
    length = len(param)
    
    

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

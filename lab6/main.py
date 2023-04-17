#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    shouldDo=True
    done = False
    regex = r'#.(\d+)?g'

    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and done == False:
                result = re.search(regex, format_string[idx:])
                if not result:
                    break
                min = result.group(1)
                fillChar = '0'
                done = True
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

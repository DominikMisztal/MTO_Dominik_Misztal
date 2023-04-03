#!/usr/bin/env python3

import sys
import re

def transform(numberString):
    transformed = []
    for num in numberString:
        up = int(num) + 1
        if(up >= 10):
            up = 0
        transformed.append(up)
    out = ''.join(str(e) for e in transformed)
    return out


def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    regex = r'#(\d+)?g'
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#':
                result = re.search(regex, format_string[idx:])
                if not result:
                    break;
                min = result.group(1)
                output = transform(param)
                
                print(param,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

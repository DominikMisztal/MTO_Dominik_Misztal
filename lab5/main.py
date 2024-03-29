#!/usr/bin/env python3

import sys
import re

def transform(numberString):
    transformed = []
    for num in numberString:
        up = int(num) - 1
        if(up < 0):
            up = 9
        transformed.append(up)
    out = ''.join(str(e) for e in transformed)
    return out


def my_printf(format_string,param):
    shouldDo=True
    done = False
    regex = r'#(\d+)?g'

    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and done == False:
                result = re.search(regex, format_string[idx:])
                if not result:
                    break
                
                min = result.group(1)
                if(min[0] == '0'):
                    fillChar = '0'
                else: 
                    fillChar = ' '
                output = transform(str(int(param)))
                if min:
                    minInt = int(min)
                    if minInt != 0 and min[0] == '0':
                        break
                    output = output.rjust(minInt, fillChar) 
                print(output,end="")
                done = True
                shouldDo=False

            else:
                print(format_string[idx],end="")

        else:
            if(format_string[idx] == 'g'):
                shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

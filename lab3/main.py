#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    shouldDo=True
    param = param.swapcase()
    regex = r'#(\d+)?(\.)?(\d+)?k'
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#':
                result = re.search(regex, format_string[idx:])
                min = result.group(1)
                dot = result.group(2)
                max = result.group(3)
                if not result:
                    break;
                if not dot and max:
                    break;
                
                if not min and not dot and not max:
                    print(param, end='')
                elif not min and dot and max:
                    maxInt = int(max)
                    if maxInt  != 0 and max[0] == '0':
                        break
                    print(f'{param:.{maxInt}}', end='')

                elif min and not dot and not max:
                    minInt = int(min)
                    if minInt != 0 and min[0] == '0':
                        break
                    print(f'{param:{minInt}}', end='')

                elif min and dot and max:
                    minInt = int(min)
                    if minInt != 0 and min[0] == '0':
                        break
                    maxInt = int(max)
                    if maxInt  != 0 and max[0] == '0':
                        break
                    print(f'{param:{minInt}.{maxInt}}', end='')


                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            if(format_string[idx] == 'k'):
                shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

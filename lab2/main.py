#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    shouldDo=True
    param = param.swapcase()
    regex = r'#(\.)+(\d+)k'
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#':
                result = re.search(regex, format_string[idx:])
                
                if not result:
                    print(format_string[idx],end="")
                    continue
                maxLen = result.group(2)
                output = param
                if max:
                    maxInt = int(maxLen)
                    if maxInt != 0 and maxLen[0] == '0':
                        break
                    output = output[0:maxInt]
                
                print(output, end='')


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
    
    

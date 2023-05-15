#!/usr/bin/env python3

import sys
import re

def transform(numberString):
    outputText = []
    for x in numberString:
        if x == 'a':
            outputText.append('g')
        elif x == 'b':
            outputText.append('h')
        elif x == 'c':
            outputText.append('i')
        elif x == 'd':
            outputText.append('j')
        elif x == 'e':
            outputText.append('k')
        elif x == 'f':
            outputText.append('l')
        else:
            outputText.append(x)
    out = ''.join(str(e) for e in outputText)
    return out

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    done = False
    regex = r'#[.](\d+)?j'
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and done == False:
                result = re.search(regex, format_string[idx:])
                if not result:
                    print(format_string[idx],end="")
                    continue

                min = result.group(1)
                fillChar = '0'
                if min:
                    minInt = int(min)
                    output = output.rjust(minInt, fillChar) 
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

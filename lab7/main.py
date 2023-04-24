#!/usr/bin/env python3

import sys

def transform(numberString):
    outputText = []
    for x in numberString:
        if x >= 'a' and x <= 'f':
            outputText.append(x+6)
        else:
            outputText.append(x)
    return str(outputText)

def my_printf(format_string,param):
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'j':
                valueHex = int(param, 16)
                string = str(hex(valueHex))
                output = transform(string)
                print(output,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

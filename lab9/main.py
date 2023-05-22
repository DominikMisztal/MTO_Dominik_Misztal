#!/usr/bin/env python3

import sys
import re

def transform(numberString):
    outputText = []
    mode = 1;
    for x in numberString:
        if x == '.':
            mode = 2;
        if x == '0':
            if mode == 1:
                outputText.append('a')
            else:
                outputText.append((0+5)%10)
        elif x == '1':
            if mode == 1:
                outputText.append('b')
            else:
                outputText.append((1+5)%10)
        elif x == '2':
            if mode == 1:
                outputText.append('c')
            else:
                outputText.append((2+5)%10)
        elif x == '2':
            if mode == 1:
                outputText.append('c')
            else:
                outputText.append((2+5)%10)
        elif x == '2':
            if mode == 1:
                outputText.append('c')
            else:
                outputText.append((2+5)%10)
        elif x == '2':
            if mode == 1:
                outputText.append('c')
            else:
                outputText.append((2+5)%10)
    out = ''.join(str(e) for e in outputText)
    return out.lower()

def my_printf(format_string,param):
    shouldDo=True
    done = False
    regex = r'#[.]+?(\d+)?h'
    regex2 = r'#j'
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and done == False:
                result = re.search(regex, format_string[idx:])
                if not result:
                    result = re.search(regex2, format_string[idx:])
                    if result:
                        output = transform(param)
                        print(output,end="")
                        done = True
                        shouldDo = False
                        continue
                    print(format_string[idx],end="")
                    continue

                min = result.group(1)
                fillChar = '0'
                output = param
                if min:
                    minInt = int(min)
                    output = output.rjust(minInt, fillChar) 
                output = transform(output)
                print(output,end="")
                done = True
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            if format_string[idx] == 'j':
                shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

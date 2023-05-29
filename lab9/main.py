#!/usr/bin/env python3

import sys
import re

def transform(numberString, precision):
    outputText = []
    substring = 's'
    for x in range(len(numberString)):
        if numberString[x] == '.':
            outputText.append('.')
            substring = numberString[(x+1):]
            break;
        if numberString[x] == '0':
            outputText.append('a')
        elif numberString[x] == '1':
            outputText.append('b')
        elif numberString[x] == '2':
            outputText.append('c')
        elif numberString[x] == '3':
            outputText.append('d')
        elif numberString[x] == '4':
            outputText.append('e')
        elif numberString[x] == '5':
            outputText.append('f')
        elif numberString[x] == '6':
            outputText.append('g')
        elif numberString[x] == '7':
            outputText.append('h')
        elif numberString[x] == '8':
            outputText.append('i')
        elif numberString[x] == '9':
            outputText.append('j')

    if len(substring) > precision:
        for x in range(precision):
            num = int(substring[x])
            if x == precision-1:
                if int(substring[x+1])>= 5:
                    outputText.append(str((num+1+5)%10))
                else:
                    outputText.append(str((num+5)%10))
            else:
                outputText.append(str((num+5)%10))
    elif len(substring) == precision:
        for x in range(precision):
            num = int(substring[x])
            outputText.append(str((num+5)%10))
    else:
        for x in range(len(substring)):
            num = int(substring[x])
            outputText.append(str((num+5)%10))
        for x in range(precision - len(substring)):
            outputText.append('5')

        
    out = ''.join(str(e) for e in outputText)
    return out.lower()


def my_printf(format_string,param):
    shouldDo=True
    done = False
    regex = r'#[.]+?(\d+)?h'
    regexFloat = r'(\d+)[.](\d+)'
    floatResult = re.search(regexFloat, param)
    if not floatResult:
        return
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and done == False:
                result = re.search(regex, format_string[idx:])
                if not result:
                    print(format_string[idx],end="")
                    continue
                
                precision = result.group(1)
                if precision:
                    precisionInt = int(precision)
                output = transform(param, precisionInt)
                print(output,end="")
                done = True
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            if format_string[idx] == 'h':
                shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

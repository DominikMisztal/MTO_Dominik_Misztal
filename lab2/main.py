#!/usr/bin/env python3

import sys

def get_num(string_nums):
    x = 0
    count = 0
    if(string_nums[x] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        return -1
    while string_nums[x] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        count += 1
        x += 1
    if string_nums[x] != 'k':
        return -2
    power = pow(10, count-1)
    x = 0
    string_len = 0
    while string_nums[x] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        string_len += power * int(string_nums[x])
        power = power/10
        x+=1
    return string_len, count
    

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == '.':
                str_len, count = get_num(format_string[idx+2:])
                print(param[:str_len].swapcase(),end="")
                shouldDo=False
                print(format_string[idx + 3 + count:],end="")
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
    
    

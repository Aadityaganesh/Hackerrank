#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    count = 0
    
    digit_found = False
    for i in password:
        if i in numbers:
            digit_found = True
            break
    if not digit_found:
        count += 1
        
    lower_found = False
    for i in password:
        if i in lower_case:
            lower_found = True
            break
    if not lower_found:
        count += 1
    
    upper_found = False
    for i in password:
        if i in upper_case:
            upper_found = True
            break
    if not upper_found:
        count += 1

    special_found = False
    for i in password:
        if i in special_characters:
            special_found = True
            break
    if not special_found:
        count += 1
    
    return max(count, 6 - n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
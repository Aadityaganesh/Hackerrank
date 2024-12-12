"""
Sample Input:
    STDIN   Function
    -----   --------
    5       t = 5
    10 10   b = 10, w = 10
    1 1 1   bc = 1, wc = 1, z = 1
    5 9     b = 5, w = 5
    2 3 4   bc = 2, wc = 3, z = 4
    3 6     b = 3, w = 6
    9 1 1   bc = 9, wc = 1, z = 1
    7 7     b = 7, w = 7
    4 2 1   bc = 4, wc = 2, z = 1
    3 3     b = 3, w = 3
    1 9 2   bc = 1, wc = 9, z = 2

Sample Output:
    20
    37
    12
    35
    12
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b, w, bc, wc, z):
    # Write your code here
    value = 0
    
    if bc <= wc:
        value += bc*b
        
        if bc + z <= wc:
            value += (bc + z)*w
        
        else:
            value += wc*w
    else:
        value += wc*w
        
        if wc + z <= bc:
            value += (wc + z)*b
        
        else:
            value += bc*b
        
    return value
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
"""
Sample Input
    STDIN           Function
    -----           --------
    7 3             arr[] size n = 7, d = 3
    1 2 4 5 7 8 10  arr = [1, 2, 4, 5, 7, 8, 10]
Sample Output
    3
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    value = 0
    
    for i in arr:
        if i + d in arr and i +d*2 in arr:
            value += 1
    
    return value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
"""
Input Format:
    The first line of the input consists of an integer .
    The next line contains  space-separated integers contained in the array.

Output Format:
    Return the integer sum of the elements in the array.

Sample Input:
    5
    1000000001 1000000002 1000000003 1000000004 1000000005

Sample Output:
    5000000015
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()    
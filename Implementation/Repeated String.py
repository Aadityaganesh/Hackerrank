"""
Sample Input 0:
    aba
    10
Sample Output 0:
    7
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    repetition = n // len(s)
    remainder = n % len(s)
    a_count = s.count('a')
    result = repetition * a_count + s[:remainder].count('a')
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)
    
    fptr.write(str(result) + '\n')

    fptr.close()
"""
Sample Input 0:
    2
    5 2 1   
    5 2 2   
Sample Output 0:
    2
    3
Explanation:
In the first query, there are n = 5 prisoners and m = 2 sweets. Distribution starts at seat number s = 1. Prisoners in seats numbered 1 and 2 get sweets. Warn prisoner 2.In the second query, distribution starts at seat 2 so prisoners in seats 2 and 3 get sweets. Warn prisoner 3
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def saveThePrisoner(n, m, s):
    # Write your code here
    result = m+s-1
    result %= n
    if result==0:
        return n
    return result
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
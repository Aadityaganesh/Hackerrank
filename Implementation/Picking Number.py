"""
Sample Input 0
    6
    4 6 5 3 3 1
Sample Output 0
    3
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    count = []
    for i in range(100):
        count.append(0)
    for num in a:
        count[num] += 1
        
    max_sum = 0
    for i in range(1, 99):
        current_sum = count[i] + count[i+1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
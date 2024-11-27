"""
Sample Input 0:
    5
    4 3 5 1 2
Sample Output 0:
    1
    3
    5
    4
    2
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    values = []
    n = len(p)
    
    for i in range(1, n+1):
        values.append(p.index(p.index(i) + 1) + 1)
        
    return values

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
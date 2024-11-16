"""
Sample Input:
    STDIN           Function
    -----           --------
    6 3             n = 6, k = 3
    1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]

Sample Output:
    5
Five pairs meet the criteria [1,2],[1,2],[3,6],[2,1] and [1,2]. Where there total is 3 and divisible by 3.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
# 

def divisibleSumPairs(n, k, ar):
    # Write your code here
    pair_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                pair_count += 1
    return pair_count                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
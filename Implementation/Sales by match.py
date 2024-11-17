"""
Sample Input:
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

Sample Output:
    3
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    new_dict = {}
    
    for number in ar:
        new_dict[number] = new_dict.get(number, 0)+1
    
    pair_count = 0
    for pairs in new_dict.values():
        pair_count += pairs//2
    
    return pair_count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
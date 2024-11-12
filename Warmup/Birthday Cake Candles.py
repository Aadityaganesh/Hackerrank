"""
Input Format:
    The first line contains a single integer, , the size of .
    The second line contains  space-separated integers, where each integer  describes the height of .

Sample Input:
    4
    3 2 1 3

Sample Output:
    2
"""

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    count = 0
    max_value = candles[0]
    for i in candles:
        if i > max_value:
            max_value = i

    for i in candles:
        if i==max_value:
            count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
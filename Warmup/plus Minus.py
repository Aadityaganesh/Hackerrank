"""
Input Format
    The first line contains an integer, , the size of the array.
    The second line contains  space-separated integers that describe .

Output Format:
    Print the following  lines, each to  decimals:
    proportion of positive values
    proportion of negative values
    proportion of zeros

Sample Input:
    STDIN           Function
    -----           --------
    6               arr[] size n = 6
    -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

Sample Output:
    0.500000
    0.333333
    0.166667
"""

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    zero = 0
    positive = 0
    negative = 0
    
    for i in arr:
        if i == 0:
            zero += 1
        elif i > 0:
            positive += 1
        elif i < 0 :
            negative += 1

    print(f"{positive / len(arr):.6f}")
    print(f"{negative / len(arr):.6f}")
    print(f"{zero / len(arr):.6f}")
             
             
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
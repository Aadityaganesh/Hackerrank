"""
Sample Input:
    STDIN       Function
    -----       --------
    5           arr[] size n = 5
    3 3 2 1 3   arr = [3, 3, 2, 1, 3]
Sample Output:
    2   
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    count = 0
    unique = set(arr)
    max_freq = 0
    
    for i in unique:
        count = 0
        for num in arr:
            if num == i:
                count+=1
        if count> max_freq:
            max_freq = count
    
    deletions = len(arr) -  max_freq
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
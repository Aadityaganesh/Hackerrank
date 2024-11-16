"""
Sample Input:
    8
    1 4 4 4 5 5 5 3
Sample Output:
    4
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    max_count = 0
    bird_type = -1
    for bird in set(arr):
        count = arr.count(bird)
        if count > max_count or (count == max_count and bird < bird_type):
            max_count = count
            bird_type = bird
    return bird_type

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
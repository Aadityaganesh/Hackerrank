"""
Sample Input:
    3
Sample Output:
    9
Explanation:
    n: the day number to report. Returns the cumulative likes at that day
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    cummulative_likes = 0
    shared = 5
    
    for i in range(n):
        like = shared//2
        cummulative_likes += like
        shared = like  *3
    
    return cummulative_likes        
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
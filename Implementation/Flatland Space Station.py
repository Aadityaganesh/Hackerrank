"""
Sample Input 0:
    STDIN   Function
    -----   --------
    5 2     n = 5, c[] size m = 2
    0 4     c = [0, 4]
Sample Output 0:
    2
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    station = sorted(c)
    value = station[0]
    
    for i in range(1, len(station)):
        value = max(value, (station[i]-station[i-1])//2)
        
    value = max(value, station[0], n - 1 - station[-1])

    return value        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
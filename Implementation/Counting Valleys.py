"""
Sample Input:
    8
    UDDDUDUU

Sample Output:
    1
Explanation:
If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:
    _/\      _
    \    /
        \/\/
The hiker enters and leaves one valley.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    level = valley = 0
    for i in path:
        if i == "U":
            level += 1
        if i == "D":
            level -= 1
        if (level == 0 and i == "U"):
            valley += 1
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
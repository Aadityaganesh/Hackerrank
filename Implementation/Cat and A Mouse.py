"""
Sample Input 0:
    2
    1 2 3
    1 3 2
Sample Output 0:
    Cat B
    Mouse C
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    A_cat = abs(x-z)
    B_cat = abs(y-z)
    
    if A_cat == B_cat:
        return "Mouse C"
    elif A_cat < B_cat:
        return "Cat A"
    else:
        return "Cat B"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
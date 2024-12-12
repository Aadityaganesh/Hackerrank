"""
Sample Input:
    STDIN   Function
    -----   --------
    1       p = 1
    100     q = 100
Sample Output:
    1 9 45 55 99
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    values = []
    for i in range(p, q+1):
        square_value = i**2
        string = str(square_value)
        middle = len(string)//2
        left = int(string[:middle]) if middle > 0 else 0
        right = int(string[middle:])
        result = left+right
        if result == i:
            values.append(i)
    if values:
        print(" ".join(map(str, values)))
    else:
        print("INVALID RANGE")
            
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
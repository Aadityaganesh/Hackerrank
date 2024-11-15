"""
Input Format:
    The first line contains a single integer, , the number of rows and columns in the square matrix .
    Each of the next  lines describes a row, , and consists of  space-separated integers .

Output Format:
    Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input:
    3
        11 2 4
        4 5 6
        10 8 -12

Sample Output:
    15
"""

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    first_diagonal = 0
    second_diagonal = 0
    for i in range(len(arr)):
        first_diagonal += arr[i][i]
        second_diagonal += arr[i][len(arr)-i-1]
     
    return abs(first_diagonal - second_diagonal)  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
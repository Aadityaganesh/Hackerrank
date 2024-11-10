"""
Input format:
    The first line contains 3 space-separated integers, a[0], a[1], and a[2], the respective values in triplet a.
    The second line contains 3 space-separated integers, b[0], b[1], and b[2], the respective values in triplet b.
Sample Input:
    5 6 7
    3 6 10

Output Format:
    Alice's score is in the first position, and Bob's score is in the second.
Sample Output:
    1 1
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice_score = 0
    bob_score = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice_score +=1 
        elif a[i] < b[i]:
            bob_score +=1
    return [alice_score, bob_score]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
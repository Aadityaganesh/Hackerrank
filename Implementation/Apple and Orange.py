"""
Input Format

The first line contains two space-separated integers denoting the respective values of s and t.
The second line contains two space-separated integers denoting the respective values of a and b.
The third line contains two space-separated integers denoting the respective values of m and n.
The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a.
The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

Output Format

Print two integers on two different lines:

The first integer: the number of apples that fall on Sam's house.
The second integer: the number of oranges that fall on Sam's house.

Sample Input:
    7 11
    5 15
    3 2
    -2 2 1
    5 -6
Sample Output:
    1
    1
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_sum = 0
    count_apple = 0
    for i in apples:
        apple_sum = a + i
        if s <= apple_sum <= t:
            count_apple+=1
    
    orange_sum = 0
    count_orange = 0
    for i in oranges:
        orange_sum = b + i
        if s <= orange_sum <= t:
            count_orange += 1
    print(count_apple)
    print(count_orange)
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
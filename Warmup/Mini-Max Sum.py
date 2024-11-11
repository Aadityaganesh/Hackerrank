"""
Input Format:
    A single line of five space-separated integers.

Output Format:
    Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input:
    1 2 3 4 5
Sample Output:
    10 14
"""

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # print(sum(arr)-max(arr),sum(arr)-min(arr))
    total_sum = sum(arr)
    min_sum = float('inf')
    max_sum = float('-inf')
    
    for num in arr:
        current_sum = total_sum - num        
        
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > max_sum:
            max_sum = current_sum
    
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
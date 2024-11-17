"""
Sample Input 0:
    4 1
    3 10 2 9
    7
Sample Output 0:
    Bon Appetit

Sample Input 1:
    4 1
    3 10 2 9
    12

Sample Output 1:
    5
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    bill.pop(k)
    bill_actual = sum(bill)//2
    charges = b - bill_actual
    if charges == 0:
        print("Bon Appetit")
    else:
        print(charges)
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
"""
Print a staircase as described above.

Input Format:
    A single integer, , denoting the size of the staircase.

Output Format:
    Print a staircase of size  using # symbols and spaces.

    Note: The last line must have  spaces in it.

Sample Input:
    6 
Sample Output:

     #
    ##
   ###
  ####
 #####
######
"""

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(n):
        print(" "*(n-i-1),end="")
        print("#"*(i+1))

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
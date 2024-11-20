"""
Sample Input 0:
    1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    abc

Sample Output 0:
    9
Assuming all letters are 1mm wide.
The tallest letter in abc is b at 3mm . The selection area for this word is 3 X 1mm X 3mm = 9mm².
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    tallest = 0
    for ele in word:
        tallest = max(tallest, h[ord(ele) - ord('a')])
    return tallest * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
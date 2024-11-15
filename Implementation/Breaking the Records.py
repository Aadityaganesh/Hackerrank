"""
Sample Input:
    9
    10 5 20 20 4 5 2 25 1
Sample Output 0
    2 4
Explanation:
She broke her best record twice (after games 2 and 7) and her worst record four times (after games 1, 4, 6, and 8), so we print 2 4 as our answer. Note that she did not break her record for best score during game , as her score during that game was not strictly greater than her best record at the time.

Sample Input 1:
    10
    3 4 21 36 10 28 35 5 24 42
Sample Output 1:
    4 0
Explanation 1:
She broke her best record four times (after games 1, 2, 3, and 9) and her worst record zero times (no score during the season was lower than the one she earned during her first game), so we print 4 0 as our answer.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    record_break = 0
    record_not_break = 0
    
    min_value = scores[0]
    max_value = scores[0]
    
    for number in range(1, len(scores)):
        if scores[number] > max_value:
            max_value = scores[number]
            record_break += 1
        elif scores[number] < min_value:
            min_value  = scores[number]
            record_not_break += 1
            
    return record_break, record_not_break

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
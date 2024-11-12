"""
Input Format:
    A single string  that represents a time in -hour clock format (i.e.:  or ).

Sample Input:
    07:05:45PM
    
Sample Output:
    19:05:45
"""

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    period = s[-2:]
    hour = int(s[:2])
    minute_second = s[2:-2]
    
    if period == "PM":
        hour = hour if hour == 12 else hour + 12
    else:
        hour = 0 if hour == 12 else hour
    
    return f"{hour:02}{minute_second}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
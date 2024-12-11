"""
Sample Input:
    4 5
    10101
    11100
    11010
    00101
Sample Output:
    5
    2
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    max_topic = 0
    max_team = 0
    
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            known = bin(int(topic[i],2)|int(topic[j],2)).count('1')
            if known > max_topic:
                max_topic = known
                max_team = 1
                
            elif known == max_topic:
                max_team +=1
                
    return [max_topic, max_team]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
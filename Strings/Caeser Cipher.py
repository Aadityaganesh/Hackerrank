#!/bin/python3

import string
#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    output = []
    k = k%26
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    
    for letter in s:
        if letter in lower_case:
            n = lower_case[(lower_case.index(letter)+k)%26]
            output.append(n)
            
        elif letter in upper_case:
            n = upper_case[(upper_case.index(letter)+k)%26]
            output.append(n)
        
        else:
            output.append(letter)
        
    return ''.join(output)           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
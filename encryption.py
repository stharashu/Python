import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    square=len(s)**0.5
    # rows = int(math.floor(square))
    columns = int(math.ceil(square))
    output = ""
    for i in range(columns):
        k = i
        for j in range(k, len(s), columns):
            output+=s[j]
        output+=" "
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()


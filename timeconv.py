import math
import os
import random
import re
import sys
from datetime import datetime
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2]
    elif s[-2:] == "AM":
        return s[:-2]
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    else:
        ans = int(s[:2]) +12
        return str(str(ans) + s[2:8])
    

# print(timeConversion)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input("1:20PM")

#     result = timeConversion(s)

#     fptr.write(result + '\n')

#     fptr.close()

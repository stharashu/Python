import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

# def is_mod_kap(num):
#     sq_num_str = str(num ** 2)
#     mid = len(sq_num_str) // 2  # floor division
#     left = sq_num_str[:mid] or 0
#     right = sq_num_str[mid:] or 0

#     return num == int(left) + int(right)

def kaprekarNumbers(p, q):
    mod_kap_nums = [str(num) for num in range(p, q + 1) if mod_kap(num)]

    if not mod_kap_nums:
        print("INVALID RANGE")
    else:
        print(' '.join(mod_kap_nums))


def mod_kap(num):
    square=str(num**2)
    mid= len(square) // 2
    left = square[:mid] or 0
    right = square[mid:] or 0
    return num == int(left) +int(right)

# def kaprekarNumbers(p, q):
#     mod_num = [str(num) for num in range(p, q+1) if mod_kap(num)]
#     if not mod_num:
#         print('Invalid')
#     else:
#         print(' '.join(mod_num))
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    if n>1:
        insertionSort2(n-1, arr)
        value = arr[n-1]
        j=n-2
        while arr[j]>value and j>=0: 
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=value
        print(" ".join(list(map(str, arr))))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

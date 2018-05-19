#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(count,a):
    diagonal1=0;
    diagonal2=0;
    for n in range(0,count):
        diagonal1=diagonal1+a[n][n];
#        print(n,count,count-n-1);
        diagonal2=diagonal2+a[n][count-n-1];
    diagonal2=diagonal2-diagonal1;
    if diagonal2<0:
        diagonal2=diagonal2*(-1);
    return diagonal2;
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []
    count=0;
    for _ in range(n):
        count=count+1;
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(count,a)

    fptr.write(str(result) + '\n')

    fptr.close()

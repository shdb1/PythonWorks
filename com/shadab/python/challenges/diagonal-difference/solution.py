#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(count,a):
    digonal1=0;
    digonal2=0;
    for n in range(0,count):
        digonal1=digonal1+a[n][n];
#        print(n,count,count-n-1);
        digonal2=digonal2+a[n][count-n-1];
    digonal2=digonal2-digonal1;
    if digonal2<0:
        digonal2=digonal2*(-1);
    return digonal2;
         

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

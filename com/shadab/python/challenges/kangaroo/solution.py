#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x2<x1 or x1<0 or x2>10000 or v1<1 or v2<1 or v1>10000 or v2>10000:
        return 'NO'
    prevDiff=x2-x1;
    while True:
        newDiff=x2-x1;
        x1=x1+v1;
        x2=x2+v2;
        if newDiff-prevDiff>0:
            return 'NO'
        if x1==x2:
            return 'YES';
        elif x1<x2:
            prevDiff=newDiff;
            continue;
        else:
            return 'NO';

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

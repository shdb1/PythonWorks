#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    sLength=len(s);
    tLength=len(t);
    loopDecider=0;
    if sLength>=tLength:
        loopDecider=tLength;
    else:
        loopDecider=sLength;
        
    breakPoint=0;
    for i in range(0,loopDecider):
        if s[i]!=t[i]:
            breakPoint=i;
            break;
    print(sLength,tLength,loopDecider,breakPoint)
    sDiff=sLength-breakPoint;
    tDiff=tLength-breakPoint;
    sDiff=sDiff+tDiff;
    if sDiff<=k:
        return 'Yes';
    else:
        return 'No';
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()

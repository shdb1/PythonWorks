#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    #
    plus=0
    minus=0;
    zeros=0;
    for item in arr:
        if item>0:
            plus=plus+1;
        elif item<0:
            minus=minus+1;
        else:
            zeros=zeros+1;
    plusfraction= plus/len(arr);
    minusFraction=minus/len(arr);
    zerosFraction=zeros/len(arr);
    print("%.6f" % plusfraction);
    print("%.6f" % minusFraction);
    print("%.6f" % zerosFraction);

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

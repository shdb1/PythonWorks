#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    #
    # Write your code here.
    #
    arr.sort();
    data=0;
    index=0;
    firstValue=0;
    lastValue=0;
    for item in arr:
        if index==0:
            firstValue=item;
        elif index==4:
            lastValue=item;
        data=data+item;
        index=index+1;
    print(data-lastValue,data-firstValue)
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

#!/bin/python3

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    #
    # Write your code here.
    #
     data='';
     for i in range(1,n+1):
        for j in range(1,n+1-i):
            data=data+' ';
        for k in range (1,i+1):
            data=data+'#'
        print(data)    
        data='';

if __name__ == '__main__':
    n = int(input())

    staircase(n)

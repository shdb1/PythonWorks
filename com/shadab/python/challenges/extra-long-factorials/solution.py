#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    output=1;
    while n>1:
        output=output*n;
        n=n-1;
    print(output)
        

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)

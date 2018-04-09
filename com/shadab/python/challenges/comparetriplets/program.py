#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the solve function below.
#

def solve(a0, a1, a2, b0, b1, b2):
    firstCandidateTotal=0;
    secondCandidateTotal=0;
    if 1 <= a0 and a0 <= 10 and 1 <= b0 and b0 <= 100:
        if a0 > b0:
            firstCandidateTotal=1;
        elif b0 > a0:
            secondCandidateTotal=1;            
    if 1 <= a1 and a1 <= 100 and 1 <= b1 and b1 <= 100:
        if a1 > b1:
            firstCandidateTotal=firstCandidateTotal+1;
        elif b1 > a1:
            secondCandidateTotal=+secondCandidateTotal1;                       
    if 1 <= a2 and a2 <= 100 and 1 <= b2 and b2 <= 100:
        if a2 > b2:
            firstCandidateTotal=firstCandidateTotal+1;
        elif b2 > a2:
            secondCandidateTotal=secondCandidateTotal+1;  
        data=(firstCandidateTotal,secondCandidateTotal);
        return data;
    
    
    
 
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = raw_input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = raw_input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)
    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()

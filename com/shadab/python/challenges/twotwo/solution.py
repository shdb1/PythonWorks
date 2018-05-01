#!/bin/python3

import os
import sys

#
# Complete the twoTwo function below.
#

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
             
    return True

def getGroups(listOfStudents):
    groups=[];
    index=0;
    while index < len(listOfStudents):
        progressiveData='';
        for k in range (index,len(listOfStudents)):
            progressiveData=progressiveData+str(listOfStudents[k]);
            groups.append(progressiveData);
        index=index+1;
    return groups;

def checkGroupStartWithZero(data):
    if int(data[0])==0:
        return True;
    else:
        return False;
    

        


def twoTwo(a):
    #
    # Write your code here.
    #
    groupData=getGroups(a);
    index=0;
    toTalTwoTwo=0;
    while(index<len(groupData)):
        startWithZero=checkGroupStartWithZero(groupData[index]);
        isSquare=isPowerOfTwo(int(groupData[index]));
        if(isSquare and startWithZero==False):
            toTalTwoTwo=toTalTwoTwo+1;
        index=index+1;
    return toTalTwoTwo;
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        result = twoTwo(a)

        fptr.write(str(result) + '\n')

    fptr.close()

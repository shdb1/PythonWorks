#!/bin/python3

import sys


def isInt(numberToCheck):
    data=str(numberToCheck).split('.')[1];
    return int(data);
    


def reverseNumber(Number):
    Reverse = 0
    while(Number > 0):
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder
        Number = Number //10
    return Reverse;

def beautifulDays(i, j, k):
    # Complete this function
    beutifulDaysCount=0;
    reversedDay=0;
    isDataInt=10000;
    for day in range(i,j+1):
        reversedDay=reverseNumber(day);
        divideResult=(reversedDay-day) / k;
        isDataInt=isInt(divideResult);
        if isDataInt==0 :
            beutifulDaysCount=beutifulDaysCount+1;
        
    return beutifulDaysCount;        
        
        
        
        

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)

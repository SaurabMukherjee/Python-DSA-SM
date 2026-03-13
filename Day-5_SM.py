### Day 5 Solving Questions on hackerrank


#Complete the function Solve me first to compute the sum of two integers
def solveMeFirst(a,b):
 return a+b
num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

### Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges,
#awarding points on a scale from 1 to 100 for three categories: problem clarity, originality,
#and difficulty.

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'compareTriplets' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b

def compareTriplets(a, b):
    total = 0
    for number in (a,b) :
        total += number
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



# Problem 4: Funny String
# HackerRank Link: https://www.hackerrank.com/challenges/funny-string/problem



import math
import os
import random
import re
import sys



def funnyString(s):
   
    r = s[::-1]
    
   
    s_diffs = [abs(ord(s[i]) - ord(s[i-1])) for i in range(1, len(s))]
    

    r_diffs = [abs(ord(r[i]) - ord(r[i-1])) for i in range(1, len(r))]
    
    if s_diffs == r_diffs:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()

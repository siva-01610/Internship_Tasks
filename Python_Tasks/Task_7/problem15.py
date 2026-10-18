# Problem 15: Game of Thrones - I
# HackerRank Link: https://www.hackerrank.com/challenges/game-of-thrones/problem



import math
import os
import random
import re
import sys


from collections import Counter

def gameOfThrones(s):
    char_counts = Counter(s)
    odd_count = 0
    
    for count in char_counts.values():
        if count % 2 != 0:
            odd_count += 1
            
    return "NO" if odd_count > 1 else "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()

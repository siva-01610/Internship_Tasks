# Problem 17: Separate the Numbers
# HackerRank Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem


import math
import os
import random
import re
import sys



def separateNumbers(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        first_str = s[:i]
        if first_str.startswith('0'):
            break
        
        current_num = int(first_str)
        built_string = first_str
        
        while len(built_string) < n:
            current_num += 1
            built_string += str(current_num)
            
        if built_string == s:
            print(f"YES {first_str}")
            return
            
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

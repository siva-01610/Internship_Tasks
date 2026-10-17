# Problem 20: Validating the Phone Number
# HackerRank Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com

import re

n = int(input())
for _ in range(n):
    number = input().strip()
    if re.match(r"^[789]\d{9}$", number):
        print("YES")
    else:
        print("NO")

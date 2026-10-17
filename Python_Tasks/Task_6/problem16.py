# Problem 16: Check Subset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-subset/problem

for i in range(int(input())):
    n1 = int(input())
    a = set(map(int, input().split()))
    n2 = int(input())
    b = set(map(int, input().split()))
    print(a.issubset(b))

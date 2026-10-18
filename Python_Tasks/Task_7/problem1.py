# Problem 1: Set .symmetric_difference() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n1 = int(input())
english = set(map(int, input().split()))
n2 = int(input())
french = set(map(int, input().split()))

print(len(english.symmetric_difference(french)))

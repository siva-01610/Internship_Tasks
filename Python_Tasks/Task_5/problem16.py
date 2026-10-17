# Problem 16: Collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())

shoe_count = Counter(shoe_sizes)
total_earnings = 0

for _ in range(num_customers):
    size, price = map(int, input().split())
    if shoe_count[size] > 0:
        shoe_count[size] -= 1
        total_earnings += price

print(total_earnings)


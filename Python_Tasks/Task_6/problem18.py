# Problem 18: Set Mutations
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
s = set(map(int, input().split()))
num_queries = int(input())

for _ in range(num_queries):
    op, length = input().split()
    other_set = set(map(int, input().split()))
    
    if op == 'update':
        s.update(other_set)
    elif op == 'intersection_update':
        s.intersection_update(other_set)
    elif op == 'difference_update':
        s.difference_update(other_set)
    elif op == 'symmetric_difference_update':
        s.symmetric_difference_update(other_set)

print(sum(s))

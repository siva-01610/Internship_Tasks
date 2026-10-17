# Problem 20: Piling Up!
# HackerRank Link: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

for _ in range(int(input())):
    n = int(input())
    blocks = deque(map(int, input().split()))
    
    current_top = float('inf')
    possible = True
    
    while blocks:
        if blocks[0] >= blocks[-1]:
            cube = blocks.popleft()
        else:
            cube = blocks.pop()
            
        if cube <= current_top:
            current_top = cube
        else:
            possible = False
            break
            
    print("Yes" if possible else "No")

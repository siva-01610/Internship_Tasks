# Problem 2: The Captain's Room
# HackerRank Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
rooms = list(map(int, input().split()))

s1 = set()  
s2 = set()  

for room in rooms:
    if room in s1:
        s2.add(room)
    else:
        s1.add(room)


print(list(s1.difference(s2))[0])

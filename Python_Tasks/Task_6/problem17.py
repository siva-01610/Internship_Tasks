# Problem 17: Check Strict Superset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

def check_strict_superset():
    a = set(input().split())
    n = int(input())
    
    result = all(a.issuperset(set(input().split())) and a != set(input().split()) for _ in range(n))
    a = set(input().split())
    n = int(input())
    
    is_strict_superset = True
    for _ in range(n):
        other = set(input().split())
        if not (a.issuperset(other) and len(a) > len(other)):
            is_strict_superset = False
            
    print(is_strict_superset)

if __name__ == '__main__':
    a = set(input().split())
    n = int(input())
    print(all(a > set(input().split()) for _ in range(n)))

# Problem 8: Tuples
# HackerRank Link: https://www.hackerrank.com/challenges/python-tuples/problem


n = int(input())
t = tuple(map(int, input().split()))

def tuple_hash(t):
    x = 0x345678
    mult = 1000003
    length = len(t)
    mask = (1 << 64) - 1

    for item in t:
        x = ((x ^ item) * mult) & mask
        if x >= (1 << 63):
            x -= (1 << 64)

        length -= 1
        mult += 82520 + length + length

    x = (x + 97531) & mask
    if x >= (1 << 63):
        x -= (1 << 64)

    if x == -1:
        x = -2

    return x

print(tuple_hash(t))

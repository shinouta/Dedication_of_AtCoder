import sys
input = sys.stdin.readline

def partition(a, p, r):
    x = a[r]
    i = p
    for j in range(p, r):
        if a[j] <= x:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i

n = int(input())
a = [int(i) for i in input().split()]
index = partition(a, 0, len(a)-1)
a[index] = [a[index]]
print(*a)

import sys
input = sys.stdin.readline

def counting_sort(a, b, k):
    c = [0]*(k+1)
    for i in range(n):
        c[a[i]] += 1
    
    for i in range(k-1):
        c[i+1] += c[i]

    for i in range(n-1, -1, -1): # aの後方からbに挿入しないと, Not stableとなる
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1

n = int(input())
a = [int(i) for i in input().split()]
b = [None]*len(a)
counting_sort(a, b, 10**4)
print(*b)

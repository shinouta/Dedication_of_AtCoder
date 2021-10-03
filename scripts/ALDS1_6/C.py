import sys
input = sys.stdin.readline

def partition(a, p, r):
    """
    [p, r)の範囲の要素を, a[r]を基準に分裂させる.
    i:= [0, i)が, a[r]以下の要素となるようなi
    j:= [i, j)が, a[r]以上の要素となるようなj
    """
    x = a[r][1]
    i = p
    for j in range(p, r):
        if a[j][1] <= x:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i

def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)

n = int(input())
a = []
for i in range(n):
    m, k = input().split()
    a.append([m, int(k), i])
quicksort(a, 0, n-1)

is_stable = "Stable"
for i in range(n-1):
    if a[i][1] == a[i+1][1] and a[i][2] > a[i+1][2]:
        is_stable = "Not stable"
print(is_stable)

for i in range(n):
    print(a[i][0], a[i][1])

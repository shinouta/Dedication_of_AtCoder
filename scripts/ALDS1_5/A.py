# TLE
def divide_and_conquer(i, m, a):
    if m == 0:
        return True
    if i >= n:
        return False
    res = divide_and_conquer(i+1, m, a) or divide_and_conquer(i+1, m - a[i], a)
    return res

n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

for num in m:
    if divide_and_conquer(0, num, a):
        print("yes")
    else:
        print("no")

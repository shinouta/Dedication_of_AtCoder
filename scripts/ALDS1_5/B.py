def merge(a, left, mid, right, INF):
    l = a[left:mid] + [INF] # 要素比較時のIndexError防止のINF
    r = a[mid:right] + [INF]
    i, j = 0, 0
    count = 0
    for k in range(left, right):
        count += 1
        if l[i] <= r[j]: # 仮に値が同じならleft側の要素を優先するのでStable
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
    return count

def merge_sort(a, left, right, INF):
    if left+1 < right: # leftのrightの間に2つの要素があればTrue
        mid = (left + right)//2
        c_l = merge_sort(a, left, mid, INF)
        c_r = merge_sort(a, mid, right, INF)
        c = merge(a, left, mid, right, INF)
        return c + c_l + c_r
    return 0

def main():
    INF = 10**9 + 1
    n = int(input())
    a = [int(i) for i in input().split()]
    count = 0
    c = merge_sort(a, 0, n, INF)
    print(*a)
    print(c)

main()

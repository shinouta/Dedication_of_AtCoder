"""
def koch(e1, e2, n):
    # 引数のe1とe2はreturnしないように設定
    # そうすることで返り値を管理しやすくした.
    if n == 0:
        return []
    ans = []
    s = [(e1[0]*2 + e2[0])/3, (e1[1]*2 + e2[1])/3]
    t = [(e1[0] + e2[0]*2)/3, (e1[1] + e2[1]*2)/3]
    u = [((s[0] + t[0]) - (t[1] - s[1])*(3**0.5))/2, ((s[1] + t[1]) + (t[0] - s[0])*(3**0.5))/2]
    return koch(e1, s, n-1)\
            + [s]\
            + koch(s, u, n-1)\
            + [u]\
            + koch(u, t, n-1)\
            + [t]\
            + koch(t, e2, n-1)\

n = int(input())
p1 = [0.0, 0.0]
p2 = [100.0, 0.0]
l = koch(p1, p2, n)
print(*p1) # 返されないので
for row in l:
    print(*row)
print(*p2) # 返されないので
"""

def koch(e1, e2, n):
    # 再帰は前の方から完結していくことを利用したprint式
    if n == 0:
        return
    s = [(e1[0]*2 + e2[0])/3, (e1[1]*2 + e2[1])/3]
    t = [(e1[0] + e2[0]*2)/3, (e1[1] + e2[1]*2)/3]
    u = [((s[0] + t[0]) - (t[1] - s[1])*(3**0.5))/2, ((s[1] + t[1]) + (t[0] - s[0])*(3**0.5))/2]

    koch(e1, s, n-1)
    print(*s)
    koch(s, u, n-1)
    print(*u)
    koch(u, t, n-1)
    print(*t)
    koch(t, e2, n-1)

n = int(input())
p1 = [0.0, 0.0]
p2 = [100.0, 0.0]
print(*p1) # 返されないので
koch(p1, p2, n)
print(*p2) # 返されないので

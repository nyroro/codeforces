import bisect
def solve():
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()

    ret = 0
    s = sum(a)
    t1 = s-x
    t2 = s-y
    # print(a, t1, t2)
    for i in range(n):
        v1 = t1 - a[i]
        j = bisect.bisect_right(a, v1)
        v2 = t2 - a[i]
        k = bisect.bisect_left(a, v2)
        if j < i:
            break
        k = max(k, i+1)
        # print(i, j, k, j-k)
        ret += max(j-k, 0)
    print(ret)
for i in range(int(input())):
    solve()
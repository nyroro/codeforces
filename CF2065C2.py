import bisect
t = int(input())
def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    a[0] = min(a[0], b[0]-a[0])
    for i in range(1,n):
        j = bisect.bisect_left(b, a[i]+a[i-1])
        if j < m:
            t = b[j]-a[i]
            if a[i]>=a[i-1]:
                a[i] = min(t, a[i])
            else:
                a[i] = t
        else:
            if a[i]>=a[i-1]:
                continue
            else:
                print('NO')
                break
    else:
        print('YES')
            

for _ in range(t):
    solve()
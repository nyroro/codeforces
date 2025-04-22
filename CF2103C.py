import heapq
def solve():
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr = [1 if t <= k else -1 for t in arr]
    p = [t for t in arr]
    for i in range(1,n):
        p[i]+=p[i-1]
    s = [t for t in arr]
    for i in range(n-2,-1,-1):
        s[i]+=s[i+1]
    # print(p)
    # print(s)
    f = False
    l = n
    v = 0x7fffffff
    for i in range(n-1):
        if p[i]>=0:
            if p[i]-v>=0:
                f=True
            v = min(p[i],v)
            l = min(l, i)
    if f:
        print('YES')
        return
    cnt = 0
    r = 0
    v = 0x7fffffff
    for i in range(n-1,0,-1):
        if s[i]>=0:
            if s[i]-v>=0:
                f=True
            v = min(s[i],v)
            r = max(r,i)
    if f:
        print('YES')
        return
    if l<r-1:
        print('YES')
        return
    print('NO')

for i in range(int(input())):
    solve()
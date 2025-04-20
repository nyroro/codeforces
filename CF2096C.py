maxn = 1000000000000000000
def solve():
    n = int(input())
    h = []
    for i in range(n):
        h.append(list(map(int,input().split())))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    dpr = [0]*2
    dpr[1] = a[0]
    for i in range(1, n):
        fu = False
        fd = False
        f = False
        ndpr = [maxn,maxn]

        for j in range(n):
            if h[i][j] == h[i-1][j]:
                f = True
            elif h[i][j] == h[i-1][j]+1:
                fd = True
            elif h[i][j]+1 == h[i-1][j]:
                fu = True
        if f and fd and fu:
            print(-1)
            return
        if not f:
            ndpr[0] = min(dpr[0],ndpr[0])
            ndpr[1] = min(dpr[1]+a[i],ndpr[1])
        if not fd:
            ndpr[0] = min(dpr[1], ndpr[0])
        if not fu:
            ndpr[1] = min(dpr[0]+a[i], ndpr[1])
        dpr = ndpr
    ret = min(dpr[0],dpr[1])

    dpr = [0]*2
    dpr[1] = b[0]
    for i in range(1, n):
        fu = False
        fd = False
        f = False
        ndpr = [maxn,maxn]

        for j in range(n):
            if h[j][i] == h[j][i-1]:
                f = True
            elif h[j][i] == h[j][i-1]+1:
                fd = True
            elif h[j][i]+1 == h[j][i-1]:
                fu = True
        if f and fd and fu:
            print(-1)
            return
        if not f:
            ndpr[0] = min(dpr[0],ndpr[0])
            ndpr[1] = min(dpr[1]+b[i],ndpr[1])
        if not fd:
            ndpr[0] = min(dpr[1], ndpr[0])
        if not fu:
            ndpr[1] = min(dpr[0]+b[i], ndpr[1])
        dpr = ndpr
    ret += min(dpr[0],dpr[1])
    if ret >= maxn:
        print(-1)
        return
    print(ret)


for i in range(int(input())):
    solve()
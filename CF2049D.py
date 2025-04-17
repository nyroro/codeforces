def solve():
    n,m,k = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    maxn = 1000000000000000000
    dp = [maxn]*m
    for i in range(m):
        g = [maxn]*m
        g[0] = k*i + a[0][i]
        dp[0] = min(g[0], dp[0])
        for j in range(1,m):
            g[j] = g[j-1]+a[0][(i+j)%m]
            dp[j] = min(g[j], dp[j])
    for i in range(1, n):
        ndp = [maxn]*m
        for j in range(m):
            g = [maxn]*m
            g[0] = k*j + a[i][j] + dp[0]
            ndp[0]=min(ndp[0],g[0])
            for kk in range(1,m):
                g[kk] = min(g[kk-1]+a[i][(j+kk)%m], k*j+a[i][(j+kk)%m]+dp[kk])
                ndp[kk]=min(ndp[kk],g[kk])
        dp = ndp
    print(dp[m-1])

for i in range(int(input())):
    solve()
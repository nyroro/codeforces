import math
mod = 998244353
def solve():
    n,m,d = map(int, input().split())
    mat = []
    for i in range(n):
        mat.append(input())
    d2 = int(math.sqrt(d**2-1))
    dp = [0]*m

    for i in range(m):
        if mat[n-1][i] == 'X':
            dp[i] = 1

    s = [0]*m
    s[0] = dp[0]
    for i in range(1, m):
        s[i] = (s[i-1]+dp[i])%mod
    
    for i in range(0, m):
        if mat[n-1][i] == 'X':
            dp[i] = s[min(m-1,i+d)]
            if i-d-1>=0:
                dp[i] = (dp[i]-s[i-d-1]+mod)%mod
        else:
            dp[i] = 0
    # print(dp)
    for i in range(n-2, -1, -1):
        s[0] = dp[0]
        for j in range(1,m):
            s[j] = (s[j-1]+dp[j])%mod
        for j in range(0, m):
            if mat[i][j] == 'X':
                dp[j] = s[min(m-1, j+d2)]
                if j-d2-1>=0:
                    dp[j] =(mod + dp[j] - s[j-d2-1])%mod
            else:
                dp[j] = 0
        s[0] = dp[0]
        for j in range(1,m):
            s[j] = (s[j-1]+dp[j])%mod
        for j in range(0, m):
            if mat[i][j] == 'X':
                dp[j] = s[min(m-1, j+d)]
                if j-d-1>=0:
                    dp[j] =(mod +dp[j]- s[j-d-1])%mod
            else:
                dp[j] = 0
        # print(dp)
    print(sum(dp)%mod)
for i in range(int(input())):
    solve()
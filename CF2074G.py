def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[0]*(n+1) for i in range(n+1)]
    ret = 0
    for l in range(n-1, -1, -1):
        for r in range(l,n):
            for k in range(l,r):
                dp[l][r] = max(dp[l][r], dp[l][k]+dp[k+1][r])
            for k in range(l+1,r):
                dp[l][r] = max(dp[l][r], dp[l+1][k-1]+dp[k+1][r-1]+arr[l]*arr[k]*arr[r])
    print(dp[0][n-1])
for i in range(int(input())):
    solve()
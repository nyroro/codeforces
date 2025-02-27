t = int(input())
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[0]*2 for _ in range(n+1)]
    for i in range(n):
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1]
        if arr[i] > 0:
            dp[i+1][0] = max(dp[i+1][0], dp[i][0] + arr[i])
        else:
            dp[i+1][1] = max(dp[i+1][1], dp[i][0]-arr[i], dp[i][1]-arr[i])
        # print(dp[i])
    print(max(dp[n]))
for _ in range(t):
    solve()
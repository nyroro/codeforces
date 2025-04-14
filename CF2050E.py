def solve():
    a = input()
    b = input()
    c = input()
    n = len(a)
    m = len(b)
    dp = [[0x7fffffff]*(n+1) for i in range(m+1)]
    dp[0][0] = 0
    for i in range(1,n+1):
        if a[i-1] == c[i-1]:
            dp[0][i] = dp[0][i-1]
        else:
            dp[0][i] = dp[0][i-1]+1
    for i in range(1,m+1):
        if b[i-1] == c[i-1]:
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][0] = dp[i-1][0]+1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if c[i+j-1] == a[j-1]:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
            else:
                dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
            if c[i+j-1] == b[i-1]:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
        # print(dp[i])
    print(dp[m][n])
            

for i in range(int(input())):
    solve()
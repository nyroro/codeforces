n = int(input())
arr = list(map(int, input().split()))
ind = [0]*(n+1)
for i,t in enumerate(arr):
    ind[t] = i

dp = [[0x7fffffff]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    dp[i][i] = 0
    if i+1<=n:
        dp[i][i+1] = abs(ind[i+1]-ind[i])

for i in range(2, n):
    for j in range(1,n-i+1):
        for k in range(j+1,j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] +dp[k][j+i])
            # print('t',k+1,j,i,abs(ind[k+1] - ind[j]), dp[j][k] , dp[k+1][j+i])
            dp[j][j+i] = min(dp[j][j+i], abs(ind[k+1] - ind[j]) + dp[j][k] + dp[k+1][j+i])
# for i in range(1,n+1):
#     print(dp[i])
print(dp[1][n])
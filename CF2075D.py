MAXN = 1<<63
dp = [[MAXN]*63 for i in range(63)]

dp[0][0] = 0
for i in range(1,63):
    for j in range(62,-1,-1):
        for k in range(62,-1,-1):
            if j>=i:
                dp[j][k] = min(dp[j][k], dp[j-i][k] + (1<<i))
            if k>=i:
                dp[j][k] = min(dp[j][k], dp[j][k-i]+(1<<i))
# for i in range(63):
#     print(dp[i])
def solve():
    x, y = map(int,input().split())
    if x<y:
        x,y = y,x
    if x==y:
        print(0)
        return
    ret = MAXN
    for i in range(62):
        for j in range(62):
            if (x>>i) == (y>>j):
                ret = min(ret, dp[i][j])
    print(ret)
    
for i in range(int(input())):
    solve()
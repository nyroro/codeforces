def solve():
    n = int(input())
    addl = []
    mull = []
    addr = []
    mulr = []
    for i in range(n):
        s = input().split()
        vl = int(s[1])
        vr = int(s[3])
        if s[0] == '+':
            addl.append(vl)
            mull.append(1)
        else:
            addl.append(0)
            mull.append(vl)
        if s[2] == '+':
            addr.append(vr)
            mulr.append(1)
        else:
            addr.append(0)
            mulr.append(vr)
    ret = 0
    dp = [[1]*2 for i in range(n+1)]
    dp[n-1][0] = mull[n-1]
    dp[n-1][1] = mulr[n-1]
    ret = addl[n-1]+addr[n-1]
    for i in range(n-2, -1, -1):
        val = addl[i]+addr[i]
        ret += val*max(dp[i+1][0],dp[i+1][1])
        dp[i][0] = max(mull[i]*dp[i+1][0], dp[i+1][0] + (mull[i]-1)*dp[i+1][1])
        dp[i][1] = max(mulr[i]*dp[i+1][1], dp[i+1][1] + (mulr[i]-1)*dp[i+1][0])
    ret += max(mull[0]*dp[1][0], dp[1][0]+(mull[0]-1)*dp[1][1])
    ret += max(mulr[0]*dp[1][1], dp[1][1]+(mulr[0]-1)*dp[1][0])
    print(ret)

for i in range(int(input())):
    solve()
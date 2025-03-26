
def solve():
    s,k = map(int,input().split())
    if s >= k*k//2:
        if s%k==0:
            print(k)
        else:
            print(max(k-2, 1))
        return
    dp = [False]*(s+1)
    ndp = [False]*(s+1)
    dp[0] = True
    dir = 1

    for i in range(k,1,-1):
        if dir == 1:
            for j in range(1,s+1):
                if 0<=j-dir*i<=s and (dp[j-dir*i] or ndp[j-dir*i]):
                    ndp[j] = True
        else:
            for j in range(s, -1, -1):
                if 0<=j-dir*i<=s and (dp[j-dir*i] or ndp[j-dir*i]):
                    ndp[j] = True
        dir *= -1
        for j in range(0,s+1):
            dp[j] = ndp[j]
            ndp[j] = False
        if dp[s]:
            print(i)
            return
    print(1)
for i in range(int(input())):
    solve()
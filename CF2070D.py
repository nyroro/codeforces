mod = 998244353
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    d = [0]*(n+1)
    p = [0]*(n+1)
    tot = [0]*n
    tot[0] = 1
    arr2 = []
    for i,t in enumerate(arr):
        j = i+2
        d[j] = d[t]+1
        p[j] = t
        arr2.append((d[j], j))
    arr2.sort()
    dp = [0]*(n+1)
    dp[1] = 1
    for d, x in arr2:
        # print(d,x)
        if d == 1:
            dp[x] = 1
        else:
            dp[x] = (tot[d-1]-dp[p[x]]+mod)%mod
        tot[d]+=dp[x]
        tot[d]%=mod
    # print(dp)
    print(sum(dp)%mod)

for i in range(int(input())):
    solve()
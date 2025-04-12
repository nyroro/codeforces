def gcd(a,b):
    if a < b:
        a,b = b,a
    while b>0:
        a,b = b,a%b
    return a
def solve():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[abs(a[i]-a[i+1]) for i in range(n-1)]]
    x = 2
    while x < n:
        dp.append([])
        for i in range(n-x):
            lx = dp[-2][i]
            rx = dp[-2][i+x//2]
            if lx == 0 and rx == 0:
                dp[-1].append(0)
                continue
            dp[-1].append(gcd(lx,rx))
        x<<=1
    ret = []
    for i in range(q):
        l,r = map(int,input().split())
        l-=1
        r-=1
        if l==r:
            ret.append(0)
        else:
            x = r-l
            i = 0
            v = 1
            rr=0
            while x > 0:
                if x&v:
                    val = dp[i][l]
                    rr = gcd(rr, val)
                    l+=v
                    x-=v
                v<<=1
                i+=1
            ret.append(rr)
    print(' '.join(str(t) for t in ret))
for i in range(int(input())):
    solve()
def solve():
    n = int(input())
    a = list(map(int,input().split()))
    s = set(a)
    q = list(s)
    if len(q) == 1:
        print(0)
        return
    arr = [[0,0] for i in range(30)]
    for t in a:
        for i in range(30):
            j = t&1
            t>>=1
            arr[i][j] += 1
    ans = 0
    for t in a:
        ret = 0
        for i in range(30):
            j = t&1
            t>>=1
            ret += arr[i][1-j]*(1<<i)
        ans = max(ret, ans)
    print(ans)
for i in range(int(input())):
    solve()
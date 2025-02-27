t = int(input())
def solve():
    n,m = map(int, input().split())
    arr = []
    for i in range(n):
        a = list(map(int, input().split()))
        s = sum(a)
        ss = sum([t*(m-i) for i,t in enumerate(a)])
        arr.append((-s,-ss))
    arr.sort()
    ans = 0
    # print(arr)
    for i,t in enumerate(arr):
        s, ss = t
        s = -s
        ss = -ss
        ans += (n-i-1)*m*s + ss
        # print(i, ans)
    print(ans)
for _ in range(t):
    solve()
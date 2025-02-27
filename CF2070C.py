def solve():
    n, k = map(int, input().split())
    s = input()
    arr = list(map(int, input().split()))
    l, r = 0, 1000000000
    def gao(x):
        op = False
        cnt = 0
        for i,t in enumerate(s):
            if arr[i]>x:
                if t=='B' and not op:
                    cnt += 1
                    op = True
                elif t=='R' and op:
                    op = False
        return cnt > k
    while l<r:
        m = (l+r)//2
        if gao(m):
            l= m+1
        else:
            r = m
    print(l)

t = int(input())
for _ in range(t):
    solve()
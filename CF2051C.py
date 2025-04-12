def solve():
    n,m,k = map(int, input().split())
    a = list(map(int,input().split()))
    q = list(map(int,input().split()))
    if k < n-1:
        print('0'*m)
    elif k == n:
        print('1'*m)
    else:
        vis = [False]*n
        for t in q:
            vis[t-1] = True
        ret = [0]*m
        for i,t in enumerate(a):
            if not vis[t-1]:
                ret[i] = 1
        print(''.join(str(t) for t in ret))
for i in range(int(input())):
    solve()
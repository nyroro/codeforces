def solve():
    n = int(input())
    ret = [0]*(2*n)
    mat = []
    s = n*(2*n+1)
    for i in range(n):
        mat.append(list(map(int,input().split())))
    for i in range(n):
        ret[i+1] = mat[0][i]
        s -= mat[0][i]
    for i in range(1,n):
        ret[n+i]=mat[i][n-1]
        s -= ret[n+i]
    ret[0]=s
    print(' '.join(str(t) for t in ret))
for i in range(int(input())):
    solve()
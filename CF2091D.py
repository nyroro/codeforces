def gao(x, n, m, k):
    r = m//(x+1)*x + m%(x+1)
    return r*n >= k

def solve():
    n,m,k = map(int, input().split())
    l = 1
    r = m
    ret = r
    while l < r:
        mid = (l+r)//2
        # print('gao', mid)
        if gao(mid, n, m, k):
            ret = mid
            r = mid
        else:
            l = mid+1
    print(ret)
for i in range(int(input())):
    solve()
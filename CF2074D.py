import math
table = {}
def gao(x, v):
    x = 11*x
    if x not in table:
        table[x] = 0
    table[x] = max(table[x], v)
def solve():
    n,m = map(int, input().split())
    x = list(map(int, input().split()))
    r = list(map(int, input().split()))
    for xx,rr in zip(x,r):
        lv = xx-rr
        rv = xx+rr
        gao(lv, 0)
        gao(rv, 0)
        gao(xx, rr*rr)
        for i in range(lv+1, xx):
            v = rr*rr-(xx-i)*(xx-i)
            gao(i, v)
            gao(2*xx-i, v)
    print(sum([(2*int(math.sqrt(t)) + 1) for t in table.values()]))
    table.clear()
    
    
for i in range(int(input())):
    solve()
    
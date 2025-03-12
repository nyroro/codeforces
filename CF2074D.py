import math
table = {}
def gao(x, v):
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
        gao(lv, 1)
        gao(rv, 1)
        gao(xx, 2*rr+1)
        for i in range(lv+1, xx):
            v = 2*int(math.sqrt(rr*rr-(xx-i)*(xx-i))) + 1
            # print(xx, i, v, math.sqrt(rr*rr-(xx-i)*(xx-i)))
            gao(i, v)
            gao(2*xx-i, v)
    print(sum(table.values()))
    table.clear()


for i in range(int(input())):
    solve()
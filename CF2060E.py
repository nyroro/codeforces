case = int(input())

def parent(x):
    t = x
    arr = [x]
    while g[t]!=t:
        t = g[t]
        arr.append(t)
    for k in arr:
        g[k] = t
    return t
def merge(u,v):
    pu = parent(u)
    pv = parent(v)
    g[pu] = pv
for ci in range(case):
    n,m1,m2 = map(int, input().split())
    edg = []
    g = [i for i in range(n)]
    for i in range(m1):
        u,v = map(int, input().split())
        edg.append((u-1,v-1))
    for i in range(m2):
        u,v = map(int, input().split())
        merge(u-1, v-1)
    ans = 0
    edg2 = []
    for u,v in edg:
        if parent(u) != parent(v):
            ans += 1
        else:
            edg2.append((u,v))
    c1 = 0
    for i in range(n):
        if parent(i) == i:
            c1 += 1
    g = [i for i in range(n)]
    for u,v in edg2:
        merge(u, v)
    c2 = 0
    for i in range(n):
        if parent(i) == i:
            c2 += 1
    print(ans + c2 - c1)

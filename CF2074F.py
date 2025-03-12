def gao(l,r):
    arr = []
    while l != 0 and l<r:
        t = l&(-l)
        if l + t <= r:
            arr.append(t)
            l+=t
        else:
            break
    while l<r:
        t = r & (-r)
        arr.append(t)
        r-=t
    return arr
def solve():
    l1,r1,l2,r2 = map(int, input().split())
    arr1 = gao(l1, r1)
    arr2 = gao(l2, r2)
    ret = 0
    for t1 in arr1:
        for t2 in arr2:
            ret += max(t1,t2) // min(t1,t2)
    print(ret)
for i in range(int(input())):
    solve()
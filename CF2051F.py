def solve():
    n,m,k = map(int,input().split())
    arr = list(map(int, input().split()))
    mid = [m,m]
    l = 0
    r = n+1
    for t in arr:
        if l > 0 and t > l:
            l += 1
        if r <= n and t < r:
            r -= 1
        if t < mid[0]:
            mid[0] = max(mid[0]-1, 1)
        elif t > mid[1]:
            mid[1] = min(mid[1]+1, n)
        else:
            l = max(l, 1)
            r = min(r, n)
            if mid[1] == t and mid[0] == t:
                mid = [n,n]
        if mid[0] <= l+1:
            mid[0] = 1
        if mid[1] >= r-1:
            mid[1] = n
        ret = mid[1]-mid[0]+1
        if l< mid[0]:
            ret += l
        if r > mid[1]:
            ret += n-r+1
        print(ret,end=" ")
        # print(mid,l,r)
    print()
        
for i in range(int(input())):
    solve()
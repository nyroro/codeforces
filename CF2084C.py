def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [0]*(n+1)
    sn = 0
    ind = [0]*(n+1)
    for i in range(n):
        c[a[i]] = b[i]
        ind[a[i]] = i
    cnt = 0
    for i in range(1,n+1):
        if i == c[c[i]]:
            cnt += 1
        if c[i] == i:
            sn += 1
    if cnt <n:
        print(-1)
        return
    if n%2!=sn:
        print(-1)
        return
    ret = []
    for i in range(n//2):
        val_a = a[i]
        val_b = b[i]

        if val_a == val_b:
            ret.append((i, n//2))
            a[i],a[n//2] = a[n//2],a[i]
            b[i],b[n//2] = b[n//2],b[i]
            ind[a[i]] = i
            ind[a[n//2]] = n//2
        else:
            tar = ind[b[i]]
            if tar != n-i-1:
                ret.append((tar, n-i-1))
                a[tar],a[n-i-1] = a[n-i-1],a[tar]
                b[tar],b[n-i-1] = b[n-i-1],b[tar]
                ind[a[tar]] = tar
                ind[a[n-i-1]] = n-i-1
    print(len(ret))
    for t in ret:
        print(t[0]+1, t[1]+1)
    

for i in range(int(input())):
    solve()
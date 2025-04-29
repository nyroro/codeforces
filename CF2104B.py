def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b = [(a[0],0)]
    for i in range(1,n):
        if a[i]>b[-1][0]:
            b.append((a[i],i))
    last = len(b)-1
    ans = [0]*n
    s = 0
    for i in range(n-1,-1,-1):
        s += a[i]
        ss = s
        while last >= 0 and b[last][1]>=i:
            last -= 1
        if last >= 0 and b[last][1]<i:
            ss = s-a[i]+b[last][0]
        
        ans[n-i-1]=max(ss,s)
    print(' '.join(str(t) for t in ans))
for i in range(int(input())):
    solve()
def solve():
    n,k = map(int, input().split())
    a = list(map(int,input().split()))
    a.sort()
    if (n - k)%2 == 0:
        l = (n-k)//2-1
        r = n-l-1
    else:
        l = (n-k)//2
        r = n-l-1
    print(a[r]-a[l]+1)
for i in range(int(input())):
    solve()
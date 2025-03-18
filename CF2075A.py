def solve():
    n,k = map(int, input().split())
    ret = 0
    if n%2==1:
        if k%2==0:
            n-=k-1
        else:
            n-=k
        ret += 1
    if k%2 != 0:
        k-=1
    ret += n//k + (1 if n%k != 0 else 0)
    print(ret)
    
for i in range(int(input())):
    solve()
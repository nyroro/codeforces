def solve():
    n,k,p = map(int,input().split())
    v = abs(k)//p + (1 if abs(k)%p!=0 else 0)
    if v <= n:
        print(v)
    else:
        print(-1)

for i in range(int(input())):
    solve()
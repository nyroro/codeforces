def solve():
    n,m,k = map(int,input().split())
    now = 0
    if m%k!=0:
        for i in range(n):
            for j in range(m):
                print(now+1, end=' ')
                now = (now+1)%k
            print()
    else:
        for i in range(n):
            for j in range(m):
                print((i+j)%k+1, end=' ')
            print()
for i in range(int(input())):
    solve()
def solve():
    l,r,d,u = map(int, input().split())
    if l == r and r == d and d == u:
        print('YES')
    else:
        print('NO')
for i in range(int(input())):
    solve()
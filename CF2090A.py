def solve():
    x,y,a = map(int, input().split())
    t = a%(x+y)
    if t < x:
        print('NO')
    else:
        print('YES')
for i in range(int(input())):
    solve()
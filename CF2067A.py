def solve():
    x,y = map(int, input().split())
    if y == x+1:
        print('YES')
    elif x>y and (x-y)%9 == 8:
        print('YES')
    else:
        print('NO')
for _ in range(int(input())):
    solve()
def solve():
    a,b,c = map(int,input().split())
    s = a+b+c
    if s%3 != 0:
        print('NO')
    elif b > s//3:
        print('NO')
    else:
        print('YES')
for i in range(int(input())):
    solve()
def solve():
    n = int(input())
    s = input()
    cp = s.count('p')
    cs = s.count('s')
    if s[0]=='s':
        cs -= 1
    if s[-1] == 'p':
        cp -= 1
    if cs == 0 or cp == 0:
        print('YES')
    else:
        print('NO')
for i in range(int(input())):
    solve()
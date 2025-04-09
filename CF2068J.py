def solve():
    n = int(input())
    s = input()
    lr = s[:n].count('R')
    rw = s[n:].count('W')
    if lr != rw:
        print('NO')
        return
    if (n-lr)%2 != 0 or (n-rw)%2!=0:
        print('NO')
        return
    wi = 0
    while s[wi] == 'W':
        wi+=1
    if wi < n-lr-wi:
        print('NO')
        return
    ri = 0
    while s[2*n-ri-1] == 'R':
        ri+=1
    if ri<n-rw-ri:
        print('NO')
        return
    print('YES')

for i in range(int(input())):
    solve()
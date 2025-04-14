def solve():
    s = input()
    v = sum(int(t) for t in s)
    if v%9==0:
        print('YES')
        return
    c2 = s.count('2')
    c3 = s.count('3')
    if c2 > 9:
        print('YES')
        return
    dp = [False]*9
    dp[v%9] = True
    for i in range(c2):
        ndp = [False]*9
        for j in range(9):
            if dp[j]:
                ndp[j] = True
                ndp[(j+2)%9] = True
        dp = ndp
        if dp[0]:
            print('YES')
            return
    for i in range(min(c3,9)):
        ndp = [False]*9
        for j in range(9):
            if dp[j]:
                ndp[j] = True
                ndp[(j+6)%9] = True
        dp = ndp
        if dp[0]:
            print('YES')
            return
    print('NO')

for i in range(int(input())):
    solve()
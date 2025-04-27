def solve():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    now = -1
    cnt = 0
    p = False
    for t in a:
        if t != now:
            if t == now+1:
                if p:
                    pass
                elif cnt >= 2:
                    p = True
            else:
                p = False
            now = t
            cnt = 1
        else:
            cnt += 1
            if cnt >= 2 and p:
                print('YES')
                return
            if cnt >= 4:
                print('YES')
                return
    print('NO')
    return
for i in range(int(input())):
    solve()
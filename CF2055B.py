def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sa = sum(a)
    sb = sum(b)
    val = 0
    for ta, tb in zip(a,b):
        if ta < tb:
            if val == 0:
                val = tb - ta
            else:
                print('NO')
                return
    for ta, tb in zip(a,b):
        if ta >= tb:
            if ta-tb<val:
                print('NO')
                return
    print('YES')
        
for i in range(int(input())):
    solve()
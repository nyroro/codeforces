import sys
t = int(input())
def solve():
    n = int(input())
    if n == -1:
        exit(1)
    arr = list(map(int, input().split()))
    arr = [(t, i) for i,t in enumerate(arr)]
    arr.sort()
    now = 1
    for t in arr:
        if t[0] == now:
            now = t[0]+1
    if now <= n:
        print('?', now, 2 if now == 1 else 1)
        sys.stdout.flush()
        x = int(input())
        print('?', now, 2 if now == 1 else 1)
        sys.stdout.flush()
        y = int(input())
        if x == 0:
            print('! A')
        else:
            print('! B')
        sys.stdout.flush()
    else:
        a, b = 0,0
        for t,i in arr:
            if t == 1:
                a = i+1
            if t == n:
                b = i+1
        
        print('?', a, b)
        sys.stdout.flush()
        x = int(input())
        print('?', b,a)
        sys.stdout.flush()
        y = int(input())

        if x >=n-1 and y>=n-1:
            print('! B')
        else:
            print('! A')
        sys.stdout.flush()



for _ in range(t):
    solve()

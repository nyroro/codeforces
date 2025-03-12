import sys
def solve():
    n = int(input())
    a = 1
    b = 2
    c = 3
    print('?',a,b,c)
    sys.stdout.flush()
    t = int(input())
    if t == -1:
        exit(1)
    while t != 0:
        print('?',a,b,t)
        sys.stdout.flush()
        t1 = int(input())
        if t1 == -1:
            exit(1)
        if t1 == 0:
            c = t
            break

        print('?',a,c,t)
        sys.stdout.flush()
        t2 = int(input())
        if t2 == -1:
            exit(1)
        if t2 == 0:
            b = t
            break
        a = t
        b = t2
        c = t1
        print('?', a,b,c)
        sys.stdout.flush()
        t = int(input())
    print('!', a, b, c)
for i in range(int(input())):
    solve()
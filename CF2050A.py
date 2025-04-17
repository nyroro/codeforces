def solve():
    n,m = map(int,input().split())
    ret = -1
    mm=m
    for i in range(n):
        s = input()
        mm -= len(s)
        if ret <0 and mm<0:
            ret = i
    if ret<0:
        ret=n
    print(ret)
for i in range(int(input())):
    solve()
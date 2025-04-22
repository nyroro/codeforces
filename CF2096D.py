def solve():
    n = int(input())
    s = 0
    t = 0
    for i in range(n):
        x,y = map(int,input().split())
        s^=x
        t^=(x+y)
    print(s, t-s)
for i in range(int(input())):
    solve()
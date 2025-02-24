t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    ax = m
    ay = m
    x, y = map(int, input().split())
    for i in range(1, n):
        x, y = map(int, input().split())
        ax += x
        ay += y
    print((ax+ay)*2)
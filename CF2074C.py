def solve(x):
    # print(x)
    if x & (-x) == x:
        print(-1)
    elif (x+1)&(-(x+1)) == x+1:
        print(-1)
    else:
        tx = x
        t = tx & (-tx)
        while tx != t:
            tx -= t
            t = tx &(-tx)
        t = tx - 1
        print(t)
for i in range(int(input())):
    x = int(input())
    solve(x)
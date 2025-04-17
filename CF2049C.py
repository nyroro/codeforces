def solve():
    n,x,y = map(int,input().split())
    x-=1
    y-=1
    arr = [0]*n
    for i in range(n):
        arr[(x+i)%n] = i%2
    if n%2==1:
        arr[x]=2
    if (y-x)%2 == 0:
        arr[x] = 2
    print(' '.join(str(t) for t in arr))
for i in range(int(input())):
    solve()
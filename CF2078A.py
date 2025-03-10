def solve():
    n,x = map(int, input().split())
    arr = list(map(int, input().split()))
    s = sum(arr)
    if s == n*x:
        print('YES')
    else:
        print('NO')
for i in range(int(input())):
    solve()
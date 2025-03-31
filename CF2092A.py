def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    x = arr[0]
    y = arr[-1]
    d = y-2*x
    print(x+d)
for i in range(int(input())):
    solve()
def solve():
    n,x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ret = 0
    r = n
    for i in range(n-1, -1, -1):
        if arr[i] * (r-i) >= x:
            ret += 1
            r = i
    print(ret)
for i in range(int(input())):
    solve()
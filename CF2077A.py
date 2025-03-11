def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    ret = []
    arr.sort()
    a0 = arr[0]
    ret.append(arr[2*n-1])
    s = 0
    for i in range(1, n):
        ret.append(arr[i])
        ret.append(arr[i+n-1])
        s += arr[i+n-1] - arr[i]
    ret.append(s+arr[2*n-1]+a0)
    ret.append(a0)
    print(' '.join([str(t) for t in ret]))
for i in range(int(input())):
    solve()
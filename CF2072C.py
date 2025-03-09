def solve():
    n,x = map(int, input().split())

    arr = [0]
    tx = x
    val = 0
    while len(arr)<n and tx > 0:
        v = tx & (-tx)
        val += v
        m = len(arr)
        for i in range(m):
            arr.append(v+arr[i])
            if len(arr) >= n:
                break
        tx -= v
    while len(arr)<n:
        arr.append(x)
    if val < x:
        arr[-1] = x

    print(' '.join([str(t) for t in arr]))
for i in range(int(input())):
    solve()
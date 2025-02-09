t = int(input())
for ti in range(t):
    n = int(input())
    s = input()
    arr = [int(t) for t in s.split()]
    ans = sum(arr)
    for l in range(n-1,0,-1):
        for i in range(l):
            arr[i] = arr[i+1]-arr[i]
        s = sum(arr[:l])
        ans = max(ans, s, -s)
    print(ans)
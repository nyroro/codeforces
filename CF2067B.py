def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0]!= arr[1]:
        print('NO')
        return
    rp = 0
    rpn = arr[0]
    for i in range(2, n, 2):
        if arr[i]==arr[i-1] and arr[i]<arr[i+1]:
            arr[i]+=1
        if arr[i] > rpn:
            rp -= min(rp, arr[i]-rpn)
            rpn = arr[i]
        if arr[i] == arr[i+1]:
            if arr[i]==arr[i-1]:
                rp += 1
        else:
            gap = arr[i+1]-arr[i]
            t = min(gap,rp)
            rp -= t
            arr[i]+=t
            if arr[i]!=arr[i+1]:
                print('NO')
                break
        rpn = arr[i+1]+1
    else:
        print('YES')

for _ in range(int(input())):
    solve()
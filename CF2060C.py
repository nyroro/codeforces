from collections import Counter
t = int(input())
for ti in range(t):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    l = 0
    r = n-1
    ans = 0
    tmp = 0
    while l<r:
        s = arr[l]+arr[r]
        if s == k:
            ans += 1
            l+=1
            r-=1
        elif s > k:
            r-=1
        else:
            l+=1
    print(ans)
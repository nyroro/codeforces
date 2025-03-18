def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    l = -1
    r = -1
    ret = 0
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            if l <0:
                l = i-1
            r = i
            ret += 1
    if ret % 2 == 1:
        print(ret//2+1)
    else:
        if arr[r]-arr[l]<r-l:
            print(ret//2+1)
        else:
            print(ret//2)
for i in range(int(input())):
    solve()
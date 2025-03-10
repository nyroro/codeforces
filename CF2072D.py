def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    v = 0
    l = 0
    r = 0
    for i in range(n):
        t = arr[i]
        vv = 0
        for j in range(i+1, n):
            if arr[j]>t:
                vv-=1
            elif arr[j]<t:
                vv+=1
            if vv > v:
                v = vv
                l = i
                r = j
    print(l+1,r+1)
for i in range(int(input())):
    solve()
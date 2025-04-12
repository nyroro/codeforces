def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ret = a[-1]
    for i in range(n-1):
        if a[i]>b[i+1]:
            ret += a[i]-b[i+1]
    print(ret)
for i in range(int(input())):
    solve()
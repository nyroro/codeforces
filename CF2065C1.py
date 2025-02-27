t = int(input())
def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a[0] = min(a[0], b[0]-a[0])
    for i in range(1,n):
        if a[i]<a[i-1] and b[0]-a[i]<a[i-1]:
            print('NO')
            break
        elif a[i]>=a[i-1] and b[0]-a[i]>=a[i-1]:
            a[i] = min(a[i], b[0]-a[i])
        else:
            a[i] = max(a[i],b[0]-a[i])
    else:
        print('YES')
            

for _ in range(t):
    solve()
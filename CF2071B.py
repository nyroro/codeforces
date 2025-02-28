import math
t = int(input())
def gao(x):
    t = int(math.sqrt(x))
    return t*t == x
def solve():
    n = int(input())
    if n == 1:
        print(-1)
        return
    if gao(n*(n+1)//2):
        print(-1)
        return
    arr = list(range(1,n+1))
    s = 0
    for i in range(1,n+1):
        s += i
        if gao(s):
            j = i-1
            if j+1<n:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            else:
                arr[j-1],arr[j] = arr[j],arr[j-1]
    print(' '.join(str(t) for t in arr))
for _ in range(t):
    solve()
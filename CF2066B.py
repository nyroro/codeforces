t = int(input())

def gao(arr):
    n = len(arr)
    mex = [False]*n
    suffix = [0]*n
    now = 0
    for i in range(n-1, -1, -1):
        if arr[i]<n:
            mex[arr[i]] = True
        while now<n and mex[now]:
            now+=1
        suffix[i] = now
    m = 0x7fffffff
    for i in range(n-1):
        m = min(m,arr[i])
        if m<suffix[i+1]:
            return False
    return True

def solve():
    n = int(input())
    arr = map(int, input().split())
    arr2 = []
    zero = False
    for t in arr:
        if t == 0 and not zero:
            arr2.append(t)
            zero = True
        elif t != 0:
            arr2.append(t)
    if not zero:
        return len(arr2)
    elif gao(arr2):
        return len(arr2)
    return len(arr2)-1
for _ in range(t):
    print(solve())
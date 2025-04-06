def solve():
    n,m,k = map(int,input().split())
    if (m+1)*k <= n:
        arr = [0]*(m+1)
        for i in range(m+1):
            arr[i] = n//(m+1) + (1 if i < n%(m+1) else 0)

        ret = []
        for i in range(m+1):
            for j in range(arr[i]):
                ret.append(j)
        print(' '.join(str(t) for t in ret))
    else:
        arr = []
        for i in range(m):
            for j in range(k):
                arr.append(j)
        x = 0
        while len(arr)<n:
            arr.append(x)
            x+=1
        print(' '.join(str(t) for t in arr))


for i in range(int(input())):
    solve()
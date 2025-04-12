def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    arr = []
    for x,y in zip(a,b):
        arr.append((x,1))
        arr.append((y,2))
    arr.sort()
    cnt = n
    bad = 0
    ret = 0
    i = 0
    while i<2*n:
        x,y = arr[i]
        if bad<=k:
            ret = max(ret,x*cnt)
        while i<2*n and arr[i][0] == x:
            if arr[i][1] == 1:
                bad += 1
            elif arr[i][1] == 2:
                bad -= 1
                cnt -= 1
            i+=1
    print(ret)

    
for i in range(int(input())):
    solve()
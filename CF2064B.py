t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    f = [0]*n
    for t in arr:
        f[t-1]+=1
    l, r= -1, -1
    ret = -1
    for i, t in enumerate(arr):
        if f[t-1] == 1:
            r = i
            if l == -1:
                l = i
        else:
            if l >=0:
                if ret == -1 or r-l>ret[1]-ret[0]:
                    ret = l,r
            l, r = -1, -1
        # print(i, l,r)
    
    if l >=0:
        if ret == -1 or r-l>ret[1]-ret[0]:
            ret = l,r
    if ret == -1:
        print(0)
    else:
        print(ret[0]+1,ret[1]+1)
t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    ans = [0]*n
    flag = True
    for i in range(n):
        s = list(map(int,input().split()))
        if flag:
            s.sort()
            for j in range(1,m):
                if s[j] - s[j-1] != n:
                    flag = False
                    break
            else:
                ans[s[0]]=i+1
    if flag:
        print(' '.join([str(i) for i in ans]))
    else:
        print(-1)
            

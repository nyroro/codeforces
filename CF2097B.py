def solve():
    n,m,k = map(int,input().split())
    a = []
    for i in range(k+1):
        x,y = map(int,input().split())
        a.append((x,y))
    table = {}
    edg = []
    cycle = [False]*(2*k)

    for i in range(k):
        px,py = a[i]
        nx,ny = a[i+1]
        if abs(px-nx) + abs(py-ny) != 2:
            print(0)
            return
        if px==nx:
            x,y = px, (py+ny)//2
            if (x,y) not in table:
                index = len(table)
                table[(x,y)] = index
            else:
                index = table[(x,y)]
            if not cycle[index]:
                cycle[index] = True
            else:
                print(0)
                return
        elif py == ny:
            x,y = (px+nx)//2, py
            if (x,y) not in table:
                index = len(table)
                table[(x,y)] = index
            else:
                index = table[(x,y)]
                
            if not cycle[index]:
                cycle[index] = True
            else:
                print(0)
                return
        else:
            x,y = px, ny
            if (x,y) not in table:
                i1 = len(table)
                table[(x,y)] = i1
            else:
                i1 = table[(x,y)]
            x,y = nx,py
            if (x,y) not in table:
                i2 = len(table)
                table[(x,y)] = i2
            else:
                i2 = table[(x,y)]
            edg.append((i1,i2))
    
    m = len(table)
    p = list(range(m))
    cnt = [0]*m
    s = [1]*m
    for i in range(m):
        if cycle[i]:
            cnt[i] = 1
    for x,y in edg:
        while p[x]!=x:
            x = p[x]
        while p[y]!=y:
            y = p[y]
        if x!=y:
            p[y] = x
            s[x] += s[y]
            cnt[x] = cnt[x]+cnt[y]+1
            cycle[x] |= cycle[y]
        else:
            cnt[x]+=1
    ret = 1
    mod = int(1e9)+7
    for i,t in enumerate(cnt):
        if p[i] == i:
            if s[i] <cnt[i]:
                print(0)
                return
            elif s[i]==cnt[i]:
                if not cycle[i]:
                    ret = (ret*2)%mod
            else:
                ret = (ret*s[i])%mod
    print(ret)

for i in range(int(input())):
    solve()
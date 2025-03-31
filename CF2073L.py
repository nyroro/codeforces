r,c,n,p = map(int,input().split())
mat = []
for i in range(r):
    mat.append(list(map(int,input().split())))

s = set()
d = [(0,1),(0,-1),(1,0),(-1,0)]
for i in range(r):
    for j in range(c):
        if 0<mat[i][j]<=p:
            for di in d:
                x = i+di[0]
                y = j+di[1]
                if 0<=x<r and 0<=y<c:
                    if mat[x][y]>0:
                        v = mat[x][y]+(p-mat[i][j])
                        if 0<v<=n and v != p:
                            # print(v,mat[x][y],p,mat[i][j])
                            s.add(v)
print(f'{len(s)}/{n-1}')
                        
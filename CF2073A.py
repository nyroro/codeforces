n,m = map(int,input().split())

mat = []
row = [0]*n
col = [0]*m
for i in range(n):
    mat.append(input())
    for j in range(m):
        if mat[i][j] == '.':
            row[i]+=1
            col[j]+=1

ret = 0
for i in range(n):
    if row[i] >= 4:
        v = row[i]
        ret += v*(v-1)*(v-2)*(v-3)
    s = 0
    for j in range(m):
        if mat[i][j] == '.':
            ret += s * (col[j]-1)*2
            if row[i] > 2:
                ret += (col[j]-1)*(row[i]-1)*(row[i]-2)*2
            s+=col[j] - 1
row,col = col,row
for i in range(m):
    if row[i] >= 4:
        v = row[i]
        ret += v*(v-1)*(v-2)*(v-3)
    s = 0
    for j in range(n):
        if mat[j][i] == '.':
            ret += s * (col[j]-1)*2
            if row[i] > 2:
                ret += (col[j]-1)*(row[i]-1)*(row[i]-2)*2
            s+=col[j] - 1
print(ret)
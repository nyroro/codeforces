def solve():
    n,m = map(int,input().split())
    mat = []
    row = [[0]*m for _ in range(n)]
    col = [[0]*m for _ in range(n)]
    for i in range(n):
        mat.append(input())
        for j in range(m):
            row[i][j] = 1 if mat[i][j]=='1' else 0
            if j > 0:
                row[i][j] += row[i][j-1]

            col[i][j] = 1 if mat[i][j] == '1' else 0
            if i > 0:
                col[i][j] += col[i-1][j]
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '1':
                if row[i][j] == j+1 or col[i][j] == i+1:
                    continue
                else:
                    print('NO')
                    return
    print('YES')
for i in range(int(input())):
    solve()
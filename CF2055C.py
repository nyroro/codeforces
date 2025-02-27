t = int(input())
def solve():
    n,m = map(int, input().split())
    arr = []
    s = input()
    for i in range(n):
        arr.append(list(map(int, input().split())))
    x, y = 0,0
    for t in s:
        if t == 'D':
            arr[x][y] = -sum(arr[x])
            x += 1
        else:
            arr[x][y] = -sum([arr[i][y] for i in range(n)])
            y += 1
    arr[-1][-1] = -sum(arr[-1])
    for i in range(n):
        print(' '.join([str(arr[i][j]) for j in range(m)]))

for _ in range(t):
    solve()
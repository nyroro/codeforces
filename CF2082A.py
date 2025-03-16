def solve():
    n,m = map(int, input().split())
    arr = []
    ret1 = 0
    for i in range(n):
        arr.append(input())
        ret1 += (1 if arr[i].count('1') %2 == 1 else 0)
    ret2 = 0
    for i in range(m):
        cnt = 0
        for j in range(n):
            if arr[j][i] == '1':
                cnt+=1
        ret2+=(1 if cnt%2 == 1 else 0)
    print(max(ret1, ret2))
for i in range(int(input())):
    solve()
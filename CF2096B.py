def solve():
    n,k = map(int,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t = sorted(list(zip(a,b)), key=lambda t:-min(t[0],t[1]))
    ret = 0
    # print(t)
    for i in range(k-1):
        ret += t[i][0]+t[i][1]
    # print(ret)
    for i in range(k-1,n):
        ret += max(t[i][0],t[i][1])
    # print(ret)
    ret += 1
    print(ret)
for i in range(int(input())):
    solve()
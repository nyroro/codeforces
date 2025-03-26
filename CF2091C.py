def solve():
    n = int(input())
    if n%2 == 0:
        print(-1)
        return
    ret = [(2*i)%n+1 for i in range(n)]
    print(' '.join([str(t) for t in ret]))

for i in range(int(input())):
    solve()
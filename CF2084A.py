def solve():
    n = int(input())
    if n%2==0:
        print(-1)
    else:
        arr = [n]+list(range(1,n))
        print(' '.join([str(t) for t in arr]))
for i in range(int(input())):
    solve()
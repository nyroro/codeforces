def solve():
    n,k = map(int, input().split())
    if k%2==1:
        arr = [n]*(n-1)
        arr.append(n-1)
    else:
        arr = [n-1]*(n-2) + [n,n-1]
    print(' '.join([str(t) for t in arr]))
for i in range(int(input())):
    solve()
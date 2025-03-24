N = 100010
p = [True]*N

for i in range(2, N):
    for j in range(i*i, N, i):
        p[j] = False

def solve():
    n = int(input())
    x = max(n//2,2)
    while not p[x]:
        x-=1
    arr = [x]
    for i in range(1, x):
        arr.append(x-i)
        if x+i <= n:
            arr.append(x+i)
        else:
            break
    if x<arr[-1]<n:
        for i in range(arr[-1]+1,n+1):
            arr.append(i)
    print(' '.join([str(t) for t in arr]))

for _ in range(int(input())):
    solve()
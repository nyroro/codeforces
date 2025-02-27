t = int(input())
def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if n == k:
        for i in range(1, n, 2):
            if arr[i] != (i+1)//2:
                print((i+1)//2)
                break
        else:
            print(k//2+1)
    else:
        for i in range(1, n-k+2):
            if arr[i]!=1:
                print(1)
                break
        else:
            print(2)
for _ in range(t):
    solve()
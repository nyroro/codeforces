t = int(input())
def solve():
    n = int(input())
    if n==6:
        print("1 1 2 3 1 2")
        return
    arr = list(range(1, n+1))
    arr[-2] = 1
    arr[-1] = 2
    print(" ".join([str(i) for i in arr]))
for _ in range(t):
    solve()
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    s = sum(arr)
    print(s - len(arr) + 1)
for i in range(int(input())):
    solve()
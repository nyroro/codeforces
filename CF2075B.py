def solve():
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    if k > 1:
        arr.sort()
        print(sum(arr[-k-1:]))
    else:
        print(max(arr[0] + max(arr[1:]), arr[-1] + max(arr[0:n-1])))
for i in range(int(input())):
    solve()
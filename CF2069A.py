def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)-1):
        if arr[i-1] == 1 and arr[i] == 0 and arr[i+1] == 1:
            print('NO')
            break
    else:
        print('YES')
for _ in range(int(input())):
    solve()
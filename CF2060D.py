t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    index = -1
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            index = i
    flag = True
    for i in range(index+1):
        m = min(arr[i], arr[i+1])
        arr[i] -= m
        arr[i+1] -= m
        if arr[i] > 0:
            flag = False
    print("YES" if flag else "NO")
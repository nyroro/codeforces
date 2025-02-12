t = int(input())
for ti in range(t):
    n = int(input())
    s = input()
    arr = [int(t) for t in s.split()]
    arr = sorted(arr)
    b = -1
    for i in range(n-2, -1, -1):
        if arr[i] == arr[i+1]:
            b = arr[i]
            arr = arr[:i] + arr[i+2:]
            break
    else:
        print(-1)
        continue
    for i in range(1, n-2):
        if arr[i]-arr[i-1]<2*b:
            print(arr[i],arr[i-1],b,b)
            break
    else:
        print(-1)
        continue
def solve():
    s = input()
    arr = [int(t) for t in s]
    n = len(arr)
    for i in range(1,n):
        for j in range(max(0,i-9), i):
            v = i-j
            if arr[i]-v > arr[j]:
                t = arr[i]-v
                for k in range(i, j, -1):
                    arr[k] = arr[k-1]
                arr[j] = t
                break
        # print(arr)
    print(''.join(str(t) for t in arr))
        
for i in range(int(input())):
    solve()
def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b, a%b
    return a
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0] == arr[1]:
        print('YES')
    else:
        arr2 = []
        for i in range(1, n):
            if arr[i]%arr[0] == 0:
                arr2.append(arr[i]//arr[0])
        if len(arr2) == 0:
            print('NO')
        else:
            t = arr2[0]
            for i in range(1, len(arr2)):
                t = gcd(arr2[i], t)
                if t == 1:
                    print('YES')
                    return
            print('NO')
        
for i in range(int(input())):
    solve()
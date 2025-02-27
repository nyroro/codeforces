t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = set(map(int, input().split()))
    arr2 = set(map(int, input().split()))
    flag = True
    if len(arr1) == 1:
        flag = len(arr2)>=3
    if len(arr2) == 1:
        flag = len(arr1)>=3
    print('YES' if flag else 'NO')
s = set()
s2 = set()
def solve():
    s.clear()
    s2.clear()
    n,m = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(m):
            if arr[i][j] not in s:
                s.add(arr[i][j])
            if arr[i][j] not in s2:
                if j + 1 < m and arr[i][j] == arr[i][j+1]:
                    s2.add(arr[i][j])
                elif i+1<n and arr[i][j] == arr[i+1][j]:
                    s2.add(arr[i][j])
    return len(s)-1 + max(len(s2)-1, 0)

for i in range(int(input())):
    print(solve())
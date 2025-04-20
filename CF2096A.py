def solve():
    n = int(input())
    s = input()
    arr = [0]*n
    t1 = n
    t2 = 1
    for i in range(n-1, 0, -1):
        if s[i-1] == '>':
            arr[i] = t1
            t1-=1
        elif s[i-1]=='<':
            arr[i] = t2
            t2 += 1
    arr[0] = t1
    print(' '.join(str(t) for t in arr))

for i in range(int(input())):
    solve()
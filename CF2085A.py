def solve():
    n,k = map(int, input().split())
    s = input()
    ss = s[::-1]
    is_same = True
    for i in range(n-1):
        if ss[i]!=ss[i+1]:
            is_same = False
            break
    if is_same:
        print('NO')
        return
    elif k == 0:
        print('YES' if s<ss else 'NO')
    else:
        print('YES')

for i in range(int(input())):
    solve()
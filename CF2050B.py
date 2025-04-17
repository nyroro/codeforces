def solve():
    n = int(input())
    a = list(map(int,input().split()))
    a1 = a[::2]
    a2 = a[1::2]
    s1 = sum(a1)
    s2 = sum(a2)
    if s1%len(a1)==0 and s2%len(a2)==0 and s1//len(a1)==s2//len(a2):
        print('YES')
    else:
        print('NO')
for i in range(int(input())):
    solve()
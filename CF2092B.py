def solve():
    n = int(input())
    s1 = input()
    s2 = input()
    ss = s1[::2]+s2[1::2]
    ss2 = s1[1::2]+s2[::2]
    c1 = ss.count('0')
    c2 = ss2.count('0')
    if n%2==0:
        print('YES' if c1 >= n//2 and c2 >= n//2 else 'NO')
    else:
        print('YES' if c1 >= n//2 +1 and c2 >= n//2 else 'NO')
for i in range(int(input())):
    solve()
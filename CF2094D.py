def solve():
    p = input()
    s = input()
    if s[0]!=p[0]:
        print('NO')
        return
    a = [1]
    for i in range(1,len(p)):
        if p[i]==p[i-1]:
            a[-1]+=1
        else:
            a.append(1)
    b = [1]
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            b[-1]+=1
        else:
            b.append(1)
    if len(a) != len(b):
        print('NO')
        return
    for x,y in zip(a,b):
        if y<x or y>2*x:
            print('NO')
            return
    print('YES')
for i in range(int(input())):
    solve()
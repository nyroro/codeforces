def solve():
    n = int(input())
    s = input()
    a = []
    b = []
    for i,t in enumerate(s):
        if t == 'A':
            a.append(i)
        else:
            b.append(i)
    
    for ai in a:
        flag = True
        for bi in b:
            if bi==n-1 and ai == 0:
                continue
            if bi>ai or (bi==0 and ai == n-1):
                flag = False
                break
        if flag:
            print('Alice')
            return
    print('Bob')
for i in range(int(input())):
    solve()
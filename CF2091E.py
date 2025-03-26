N = 10000002
p = [True]*N
plist = []
for i in range(2, N):
    if p[i]:
        for j in range(i*i, N, i):
            p[j] = False
        plist.append(i)

for i in range(int(input())):
    n = int(input())
    ret = 0
    
    for t in plist:
        if t>n:
            break
        ret += n//t
    print(ret)
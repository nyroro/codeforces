n,m,t = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ret = 0
for i in range(m):
    l = b[i]-1
    r = b[i+1]-1 if i+1<m else n
    tt = t
    for j in range(l,r):
        ret = max(ret, j-l+tt//a[j])
        tt = tt-a[j]
        if tt < 0:
            break

for i in range(m-1,-1,-1):
    l = b[i]-1
    r = b[i-1]-1 if i-1>=0 else -1
    tt = t
    for j in range(l,r, -1):
        ret = max(ret, l-j+tt//a[j])
        tt-=a[j]
        if tt<0:
            break
print(ret)

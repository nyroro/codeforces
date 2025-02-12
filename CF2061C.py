tt = int(input())
mod = 998244353
for ti in range(tt):
    n = int(input())
    s = input()
    arr = [int(t) for t in s.split()]
    t = 1 if arr[0] == 0 else 0
    f = 1

    for i in range(1, n):
        nf = t
        nt = 0
        if arr[i] == arr[i-1]:
            nt = t
        if i-2>=0 and arr[i] == arr[i-2]+1:
            nt = (nt + f)%mod
        if i-2<0 and arr[i] == 1:
            nt += f
        t,f = nt,nf
    print((t + f)%mod)
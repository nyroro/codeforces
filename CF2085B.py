def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    zero = []
    for i in range(n):
        if arr[i] == 0:
            zero.append(i)
    if len(zero) == n:
        print(3)
        print(1,n//2)
        print(2,n-n//2+1)
        print(1,2)
    else:
        ans = []
        i = 0
        m = 0
        while i<n:
            if arr[i] != 0:
                i+=1
            elif i+1<n:
                if i+2 == n-1 and arr[i+2] == 0:
                    ans.append([i-m,i+2-m])
                    m+=2
                    i+=3
                else:
                    ans.append([i-m,i+1-m])
                    m+=1
                    i+=2
            else:
                ans.append([i-1-m,i-m])
                m+=1
                i+=1
        ans.append([0,n-m-1])
        print(len(ans))
        for t in ans:
            print(t[0]+1,t[1]+1)


for i in range(int(input())):
    solve()
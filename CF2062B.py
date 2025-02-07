t = int(input())
for ti in range(t):
    n = int(input())
    s = input()
    arr = [int(t) for t in s.split()]
    ans = any(arr[i]<= 2*i or arr[i]<= 2*(n-i-1) for i in range(n))
    print("YES" if not ans else "NO")
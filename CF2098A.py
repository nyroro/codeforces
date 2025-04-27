from collections import Counter
def solve():
    s = input()
    c = Counter(s)
    arr = [-1]*10
    for i in range(9, -1, -1):
        if str(i) in c:
            arr[9-i] = i
            c[str(i)] -= 1
    
    for i in range(10):
        if arr[i] < 0:
            mx = 9-i
            # print(i, mx, c)
            for j in range(mx, 10):
                if c[str(j)] > 0:
                    c[str(j)] -= 1
                    arr[i] = j
                    break
    print(''.join(str(t) for t in arr))
for i in range(int(input())):
    solve()
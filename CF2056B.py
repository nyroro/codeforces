t = int(input())
for _ in range(t):
    n = int(input())
    ans = [0] * n
    for i in range(n):
        s = input()
        x = s[i+1:].count('0')
        for j in range(n):
            if ans[j] == 0:
                if x <= 0:
                    ans[j] = i+1
                    break
                else:
                    x-=1
    print(' '.join([str(i) for i in ans]))
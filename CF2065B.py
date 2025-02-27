t = int(input())
for _ in range(t):
    s = input()
    flag = False
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            flag = True
    if flag:
        print(1)
    else:
        print(len(s))
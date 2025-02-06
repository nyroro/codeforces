
s = input()

def gao(s):
    arr = s.replace('-', '+').split('+')
    if any([len(t)>10 or len(t) == 0 or (len(t)>1 and t[0]=='0') for t in arr]):
        return None
    try:
        return eval(s)
    except:
        return None
def judge(s):
    a, b = s.split('=')
    va = gao(a)
    if va is None:
        return False
    vb = gao(b)
    if vb is None:
        return False
    return va == vb

if judge(s):
    print('Correct')
else:
    for i in range(len(s)):
        if s[i].isdigit():
            for j in range(len(s)):
                if i != j:
                    if i<j:
                        s2 = s[:i] + s[i+1:j] + s[i] + s[j:]
                    elif i>j:
                        s2 = s[:j] + s[i] + s[j:i] + s[i+1:]
                    if judge(s2):
                        print(s2)
                        exit()
    print('Impossible')
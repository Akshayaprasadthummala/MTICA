def removeSpecialChar(s):
    ans=[]
    for i in s:
        if i in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            ans.append(i)
    return ''.join(ans)       
inp=input()
print(removeSpecialChar(inp))

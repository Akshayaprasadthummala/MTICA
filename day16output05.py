def printresult(s):
    return[i[::-1] for i in s]

inp=input().strip().split()

print(*printresult(inp))

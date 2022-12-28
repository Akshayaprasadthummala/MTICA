ans=[]
for i in range(1,101):
    for j in range(2,10):
        if i%j==0:
##    if i%2==0 or i%3==0 or i%4==0:
          ans.append(i)
          break
print(*ans)

lstEven=[]
lstOdd=[]
while(True):
     inpNum=int(input("enter a value(-1 to end):"))
     if inpNum==-1:
         break
     elif inpNum%2==0:
        lstEven.append(inpNum)
     elif inpNum%2==1:
         lstOdd.append(inpNum)
          
print("Even:",*lstEven)
print("min:",min(lstEven))
print("max:",max(lstEven))
print("avg:",round(sum(lstEven)/len(lstEven),1))

print("Even:",*lstOdd)
print("min:",min(lstOdd))
print("max:",max(lstOdd))
print("avg:",round(sum(lstOdd)/len(lstOdd),1))

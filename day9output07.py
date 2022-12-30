def printday(dn):
    if(dn==1):
        return "Sunday"
    elif(dn==2):
        return "Monday"
    elif(dn==3):
        return "Tuesday"
    elif(dn==4):
        return "Wednesday"
    elif(dn==5):
        return "Thursday"
    elif(dn==6):
        return "Friday"
    elif(dn==7):
        return "Saturday"
    else:
        return "Invalid"
    
def printday1(dn):
    if(dn==1):
        return "Sunday"
    elif(dn==2):
        return "Monday"
    elif(dn==3):
        return "Tuesday"
    elif(dn==4):
        return "Wednesday"
    elif(dn==5):
        return "Thursday"
    elif(dn==6):
        return "Friday"
    elif(dn==7):
        return "Saturday"
    else:
        return "Invalid"    
import time
for i in range(7):
    inpNum=int(input())
    start=time.time()
    print(printday(inpNum))
    print((time.time()-start)*10000000)
    start=time.time()
    print(printday1(inpNum))
    print((time.time()-start)*10000000)
    

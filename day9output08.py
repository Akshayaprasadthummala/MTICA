def printMonth(dn):
    if(dn==1):
        return "January"
    elif(dn==2):
        return "February"
    elif(dn==3):
        return "March"
    elif(dn==4):
        return "April"
    elif(dn==5):
        return "May"
    elif(dn==6):
        return "June"
    elif(dn==7):
        return "July"
    elif(dn==8):
        return "August"
    elif(dn==9):
        return "Sepetember"
    elif(dn==10):
        return "October"
    elif(dn==11):
        return "November"
    elif(dn==12):
        return "December"
    else:
        return "Invalid"

def printMonth1(dn):
    if(dn==1):
        return "January"
    if(dn==2):
        return "February"
    if(dn==3):
        return "March"
    if(dn==4):
        return "April"
    if(dn==5):
        return "May"
    if(dn==6):
        return "June"
    if(dn==7):
        return "July"
    if(dn==8):
        return "August"
    if(dn==9):
        return "Sepetember"
    if(dn==10):
        return "October"
    if(dn==11):
        return "November"
    if(dn==12):
        return "December"
    else:
        return "Invalid"    
import time    
for i in range(3):
    
    inpNum=int(input())
    start=time.time()
    print(printMonth(inpNum))
    print(time.time()-start)
    start=time.time()
    print(printMonth1(inpNum))
    print(time.time()-start)

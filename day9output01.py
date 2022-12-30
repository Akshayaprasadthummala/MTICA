def printseriesDecreasing(ch,n):
    assert isinstance(ch,str),'first argument should be string'
    assert isinstance(n,int),'second argument should be int'
    for i in range(n,0,-1):
        print(ch*i)
    return None    


inpch=input("enter a character:")
inpNum=int(input("enter a no:"))
print('-'*40)
try:
    printSeriesDecreasing(inpch,inpNum)
except AssertionError as ob:
    print(ob)
  

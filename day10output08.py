fo1=open(r"D:\pythonpractice02\day10.txt","r")
fo2=open(r"D:\pythonpractice02\day10a.txt","w+")
temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("file copied")


fo=open(r"D:\pythonpractice02\day10.txt","a")
for i in range(5):
    inpstr=input("enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("written to file")

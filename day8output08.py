num1=input("enter a number:")
num2=input("enter a number:")
try:
    res=int(num1)/int(num2)#execute with num2=non zero and zero
except (ZeroDivisionError,ValueError):
    print("Exception handled by archu")

except Exception as ob:
    print(ob)
else:
    print(num1,'/',num2,'=',res)
finally:
    print('thanks')

print("visit again at python class at MTICA")    


    

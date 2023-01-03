class Number:
    def __init__(self,n):
        self.n=n
    def checkEven(self):
        if self.n/2==0:
            return "even"
        res=1
        for i in range(1,self.n+1):
            res*=i
        return res

inp=int(input())
obj=Number(inp)
print('Factorial of',inp,'is',obj.calculateFactorial())

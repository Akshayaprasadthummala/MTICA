class A:
    def first_method(self):
        print("method of class A...")
class B(A):
    def first_method(self):
        print("method of class B...")
        super().first_method()

ob=B()
ob.first_method()

        


        
        

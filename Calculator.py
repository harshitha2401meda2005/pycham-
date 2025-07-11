class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        try:
            print(a/b)
        except:
            print("Error: Division by zero is not allowed.")
l=Calculator(15,20)
print(l.addition(15,20))
print(l.subtraction(15,20))
print(l.multiplication(15,20))
print(l.division(15,20))
print(l.division(15,0))


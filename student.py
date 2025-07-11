class product:
    def __init__(self,name,price ):
        self.name = name
        self.price=price
    def getname(self):
        print(self.name)
    def getprice(self):
        print(self.age)
name=input("Enter your name:")
price=float(input("Enter your price:"))
product=product(name,price)

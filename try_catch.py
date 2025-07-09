def divi(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("You can't divide by zero")
m=int(input("enter num1: "))
n=int(input("enter num2: "))
divi(m,n)
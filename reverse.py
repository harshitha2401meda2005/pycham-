def rev(r):
    r=r[::-1]
    print(r)
    a=sum(r)
    print(a)
    print(a/5)

l=[]
for i in range(5):
    n=int(input(f"Enter number {i}: "))
    l.append(n)
rev(l)

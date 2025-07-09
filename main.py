import grades
if __name__=="__main__":
    l=[]
    for i in range(5):
        print("Enter mark: ")
        n=int(input())
        if n<100 and n>0:
            l.append(n)
        else:
            print("Invalid input")
            break
    a=sum(l)/len(l)
    grades.grades_classify(a)

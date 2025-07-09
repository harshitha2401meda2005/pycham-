import grades
if __name__=="__main__":
    l=list(map(int,input("Enter marks : ").split()))
    a=sum(l)/len(l)
    grades.grades_classify(a)

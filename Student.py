class Student:
    def __init__(self,marks):
        self.marks = marks
        self.__name = ""
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_marks(self,marks):
        if self.marks > 0 or self.marks <= 100:
            print(self.marks)
        else:
            print("Marks should be between 0 and 100")
l=Student(100)
l.set_name("LIKHITHA")
print(l.get_name())
l.set_marks(100)
l.set_marks(-50)

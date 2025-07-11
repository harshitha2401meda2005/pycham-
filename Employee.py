class Employee:
    def __init__(self,name=None,salary=None,age=None):
        self.__name=None
        self.__salary=None
        self.__age=None
        if name is not None:
            self.set_name(name)
        if salary is not None:
            self.set_salary(salary)
        if age is not None:
            self.set_age(age)
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_salary(self,salary):
        if salary > 0:
            self.__salary=float(salary)
        else:
            print("Error: Salary must  be greater than zero")
    def get_salary(self):
        return self.__salary
    def set_age(self,age):
        if 18 <= age <= 100:
            self.__age=int(age)
        else:
            print("Error: Age must be between 18 and 100")
    def get_age(self):
        return self.__age
emp=Employee()
emp.set_name("John Doe")
emp.set_salary(50000)
emp.set_age(18)
print("Employee Name:",emp.get_name())
print("Employee salary:",emp.get_salary())
print("Employee age:",emp.get_age())
emp.set_salary(-1000)



class employee:
    def work(self):
        print("work")
class manager(employee):
    def manager(self):
        print("manager")
b=manager()
b.work()
b.manager()
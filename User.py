class user:
    def login(self):
        print("login")

class BusinessUser(user):
    def run_add(self):
        print("run add")

b = BusinessUser()
b.login()
b.run_add()
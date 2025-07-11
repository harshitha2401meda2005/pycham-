class account():
    def getBalance(self):
        return self.__balance
    def setBalance(self,balance):
        self.__balance += balance
acc =Accoun(name:"abc",age:10)
print(acc.getBalance())
acc.setBalance(100)
print(acc.getBalance())
acc.setBalance(100)
print(acc.getBalance())
print(acc.__balance)
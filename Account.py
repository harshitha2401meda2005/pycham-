class Marks:
    def __init__(self,name,matm):
        self.name=name
        self.__matm=matm
    def getmarks(self,add):
        self.__matm=add
    def display(self):
        print(self.name,self.__matm)
name=Marks(name="likhitha",matm=999)
name.getmarks(1000)
name.display()

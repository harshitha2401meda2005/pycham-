class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Dog sound bow")
class cat(Animal):
    def make_sound(self):
        print("cat sound meow")
for v in [Dog(),cat()]:
    v.make_sound()

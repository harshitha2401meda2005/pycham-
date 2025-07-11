class vehicle:
    def navigate(self):
        pass
class car(vehicle):
    def navigate(self):
        print("navigate via car ")


class Bicycle(vehicle):
    def navigate(self):
        print("navigate via bicycle ")

for v in [car(), Bicycle()]:
    v.navigate()


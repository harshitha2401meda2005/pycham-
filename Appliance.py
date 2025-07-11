from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
class WashingMachine(Appliance):
    def turn_off(self):
        print("WashingMachine is now running.")
class Fridge(Appliance):
    def turn_off(self):
        print("Fridge is now cooling.")
